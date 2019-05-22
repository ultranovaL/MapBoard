from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GeoObject.Lines.PathItem import PathItem
from math import *


class MileageRoadItem(PathItem):
    def __init__(self, line, width=6):
        # 设10dpi=1mm
        super(MileageRoadItem, self).__init__(line, width)
        self.width = width
        self.distances = self.fill_distance_list()
        self.distances_sum_j = self.distance_sum_j()
        self.gaps = self.cal_gap()  # 里程碑们线段号和gap的列表

    def shape(self):
        stroke = QPainterPathStroker()
        stroke.setWidth(18)
        return stroke.createStroke(self.path)

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pen1 = QPen(QColor(185, 131, 33), 4, Qt.SolidLine)
        pen1.setCapStyle(Qt.FlatCap)
        pen1.setJoinStyle(Qt.RoundJoin)

        pen2 = QPen(Qt.black, self.width, Qt.SolidLine)
        pen2.setJoinStyle(Qt.RoundJoin)
        pen2.setCapStyle(Qt.FlatCap)

        pen3 = None
        return pen1, pen2, pen3

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        pen1, pen2, pen3 = self.define_pen()
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.draw_line(painter, pen3, pen2, pen1)
        self.draw_milestone(painter)

    def draw_line(self, painter, *pens):
        # 按照画笔传入顺序绘制，先绘制的在底层，后面依次叠甲覆盖
        for pen in pens:
            if pen is not None:
                painter.setPen(pen)
                painter.drawPath(self.path)

    def draw_milestone(self, painter: QPainter):
        coords = self.cal_obj_coord()
        path = QPainterPath()
        painter.setPen(QPen(Qt.red, 1))
        painter.setBrush(QBrush(Qt.red))
        for coord in coords:
            angle = coord[-1]
            x_center, y_center = self.pos_obj(coord[0], coord[1], 0, -16, angle)
            path.moveTo(*self.pos_obj(coord[0], coord[1], 0, -3, angle))
            path.lineTo(*self.pos_obj(coord[0], coord[1], 0, -15, angle))
            painter.drawPath(path)
            painter.drawEllipse(x_center - 2, y_center - 2, 4, 4)

    def pos_obj(self, x0, y0, dx, dy, angle):
        l = (dy ** 2 + dx ** 2) ** 0.5
        angle_old = atan2(dy, dx)
        angle_new = angle_old + angle
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

    def cal_gap(self):
        poses = []
        sum_len = self.distances_sum_j[-1]
        len1 = sum_len / 3
        len2 = 2 * sum_len / 3
        for j in range(len(self.distances_sum_j)):
            if self.distances_sum_j[j] > len1:
                pos1 = self.distances_sum_j.index(self.distances_sum_j[j])
                if j < 1:
                    gap = len1
                else:
                    gap = len1 - self.distances_sum_j[j - 1]
                poses.append((pos1, gap))
                break
        for j in range(len(self.distances_sum_j)):
            if self.distances_sum_j[j] > len2:
                pos2 = self.distances_sum_j.index(self.distances_sum_j[j])
                if j < 1:
                    gap = len2
                else:
                    gap = len2 - self.distances_sum_j[j - 1]
                poses.append((pos2, gap))
                break
        return poses

    #
    def cal_angle(self, index):  # 计算图标所在线段的与水平的角度
        angle = atan2((self.line[index + 1].y() - self.line[index].y()),
                      (self.line[index + 1].x() - self.line[index].x()))
        return angle

    def cal_obj_coord(self):
        coords_object = []
        for point_index, gap in self.gaps:
            angle = self.cal_angle(point_index)
            x1, y1 = self.line[point_index].x(), self.line[point_index].y()
            x_obj, y_obj = x1 + gap * cos(angle), y1 + gap * sin(angle)
            coords_object.append((x_obj, y_obj, angle))
        return coords_object
