from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GeoObject.Points.PointItem import PointItem


class ChuYouGuan(PointItem):
    def __init__(self, x, y):
        super(ChuYouGuan, self).__init__(x, y)
        self.r = 60
        self.line_width = self.r / 6

    def boundingRect(self):
        return QRectF(self.x - self.r - 10, self.y - self.r - 10, 2 * self.r + 20, 2 * self.r + 20)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, self.line_width))
        painter.setBrush(QBrush(Qt.white))
        circle = self.cal_circle(self.x, self.y, self.r)
        painter.drawEllipse(*circle)
        painter.setPen(QPen(Qt.black, self.line_width))
        painter.setBrush(QBrush(Qt.black))
        painter.drawPie(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2, 0, 180 * 16)

    def cal_circle(self, x, y, r):
        x1 = x - r
        y1 = y - r
        w = 2 * r
        h = 2 * r
        return [x1, y1, w, h]
