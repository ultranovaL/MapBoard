from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *


class Plane(QGraphicsItem):
    def __init__(self, line):
        super(Plane, self).__init__()
        self.line = line
        self.size = 30
        self.distances = self.fill_distance_list()  # 每条线段的长度
        self.distances_sum_j = self.distance_sum_j()
        self.x, self.y = self.cal_plane_coord()
        self.r = self.size / 2

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRectF(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)
        painter.drawEllipse(self.x - self.r, self.y - self.r, self.size, self.size)

    def fill_distance_list(self):  # 计算每段线段的长度写入列表
        points = self.line
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
        return angle

    def cal_plane_coord(self):  # 计算飞机图标的坐标
        gap, point_index = self.cal_gap()
        angle = self.cal_angle(point_index)
        x1, y1 = self.line[point_index].x(), self.line[point_index].y()
        x_plane, y_plane = x1 + gap * cos(angle), y1 + gap * sin(angle)
        return x_plane, y_plane
