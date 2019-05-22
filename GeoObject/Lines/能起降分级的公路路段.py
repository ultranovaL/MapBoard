from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GeoObject.Lines.PathItem import PathItem
from math import *


class PlaneRoadItem(PathItem):
    def __init__(self, line, width=10):
        # 设10dpi=1mm
        super(PlaneRoadItem, self).__init__(line, width)
        self.width = width
        self.distances = self.fill_distance_list()  # 每条线段的长度
        self.distances_sum_j = self.distance_sum_j()
        self.angle = 0

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pen1 = QPen(Qt.white, 3, Qt.SolidLine)
        pen1.setCapStyle(Qt.FlatCap)
        pen1.setJoinStyle(Qt.RoundJoin)
        pen2 = QPen(Qt.red, self.width, Qt.SolidLine)
        pen2.setJoinStyle(Qt.RoundJoin)
        pen2.setCapStyle(Qt.FlatCap)
        pen3 = None
        return pen1, pen2, pen3

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        pen1, pen2, pen3 = self.define_pen()
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.draw_line(painter, pen3, pen2, pen1)
        self.draw_circle(painter)
        self.draw_plane(painter)
        self.draw_sideline(painter)

    def draw_line(self, painter, *pens):
        # 按照画笔传入顺序绘制，先绘制的在底层，后面依次叠甲覆盖
        for pen in pens:
            if pen is not None:
                painter.setPen(pen)
                painter.drawPath(self.path)

    def draw_circle(self, painter: QPainter):
        x, y = self.cal_plane_coord()
        r = 15
        # 图标外圆圈
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(Qt.white)
        painter.drawEllipse(x - r, y - r, 2 * r, 2 * r)

    def draw_plane(self, painter: QPainter):
        # 机身
        painter.setPen(QPen(Qt.black))
        painter.setBrush(Qt.black)
        path = QPainterPath()
        path.moveTo(*self.pos_plane(14, 0))
        path.lineTo(*self.pos_plane(13, 1.5))
        path.lineTo(*self.pos_plane(12, 2))
        path.lineTo(*self.pos_plane(7, 3))
        path.lineTo(*self.pos_plane(0, 13))
        path.lineTo(*self.pos_plane(-4, 14))
        path.lineTo(*self.pos_plane(0, 4))
        path.lineTo(*self.pos_plane(-10, 3))
        path.lineTo(*self.pos_plane(-12, 7))
        path.lineTo(*self.pos_plane(-13, 7))
        path.lineTo(*self.pos_plane(-11, 0))
        path.lineTo(*self.pos_plane(-13, -7))
        path.lineTo(*self.pos_plane(-12, -7))
        path.lineTo(*self.pos_plane(-10, -3))
        path.lineTo(*self.pos_plane(0, -4))
        path.lineTo(*self.pos_plane(-4, -14))
        path.lineTo(*self.pos_plane(0, -13))
        path.lineTo(*self.pos_plane(7, -3))
        path.lineTo(*self.pos_plane(12, -2))
        path.lineTo(*self.pos_plane(13, -1.5))
        painter.drawPath(path)

    def draw_sideline(self, painter: QPainter):
        x, y = self.cal_plane_coord()
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(Qt.white)
        path = QPainterPath()
        path.moveTo(*(self.pos_plane(-45, 10)))
        path.lineTo(*(self.pos_plane(-45, -10)))
        path.moveTo(*(self.pos_plane(45, 10)))
        path.lineTo(*(self.pos_plane(45, -10)))
        painter.drawPath(path)

    def pos_plane(self, dx, dy):
        x0, y0 = self.cal_plane_coord()
        l = (dy ** 2 + dx ** 2) ** 0.5
        angle_old = atan2(dy, dx)
        angle_new = angle_old + self.angle
        x2 = x0 + l * cos(angle_new)
        y2 = y0 + l * sin(angle_new)
        return x2, y2

    def fill_distance_list(self):  # 计算每段线段的长度写入列表
        points = self.line.copy()
        distance_list = []
        for i in range(len(points) - 1):
            x1, y1 = points[i].x(), points[i].y()
            x2, y2 = points[i + 1].x(), points[i + 1].y()
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            distance_list.append(distance)
        return distance_list

    def distance_sum_j(self):  # 计算前j段的距离和，j=0，1，2，3...
        tmp_distance = 0
        list_dis = []
        for i in range(len(self.distances)):
            tmp_distance += self.distances[i]
            list_dis.append(tmp_distance)
        return list_dis

    def dichotomy(self, low, high, middle_dis):  # 二分法求中点所在线段的编号
        while low < high:
            mid_num = int((low + high) / 2)
            if self.distances_sum_j[mid_num] < middle_dis:
                low = mid_num + 1
            else:
                high = mid_num
        return high

    def cal_gap(self):  # 二分法计算图标坐标与上一个节点间的距离
        middle_dis = self.distances_sum_j[-1] / 2
        high = len(self.distances_sum_j)
        pos = self.dichotomy(0, high, middle_dis)
        # 第pos条折线的长度
        if pos < 1:
            len_pos = 0
        else:
            len_pos = self.distances_sum_j[pos - 1]
        # 中点距离第pos条折线起点的距离
        dis = middle_dis - len_pos
        return dis, pos

    def cal_angle(self, index):  # 计算图标所在线段的与水平的角度
        angle = atan2((self.line[index + 1].y() - self.line[index].y()),
                      (self.line[index + 1].x() - self.line[index].x()))
        self.angle = angle
        return angle

    def cal_plane_coord(self):  # 计算飞机图标中心的坐标
        gap, point_index = self.cal_gap()
        angle = self.cal_angle(point_index)
        x1, y1 = self.line[point_index].x(), self.line[point_index].y()
        x_plane, y_plane = x1 + gap * cos(angle), y1 + gap * sin(angle)
        return x_plane, y_plane
