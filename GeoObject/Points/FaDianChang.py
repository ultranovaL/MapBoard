from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
from GeoObject.Points.PointItem import PointItem


class FaDianChang(PointItem):
    def __init__(self, x, y):
        super(FaDianChang, self).__init__(x, y)
        self.rad = pi / 180
        self.size = 150
        self.len_arrow = self.size / 5

    def boundingRect(self):
        return QRectF(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(self.x - 0.2 * self.size, self.y - 0.2 * self.size, 0.4 * self.size, 0.4 * self.size)

        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush())
        for i in range(0, 4):
            x0, y0 = self.x, self.y
            length = self.len_arrow
            x1, y1 = x0 + self.size / 2 * 2 ** 0.5 * sin((45 + 90 * i) * self.rad), y0 + self.size / 2 * 2 ** 0.5 * cos(
                (45 + 90 * i) * self.rad)
            angle = 30 * self.rad
            x2, y2 = x1 - length * cos(atan2((y1 - y0), (x1 - x0)) - angle), y1 - length * sin(
                atan2((y1 - y0), (x1 - x0)) - angle)
            x3, y3 = x1 - length * sin(atan2((x1 - x0), (y1 - y0)) - angle), y1 - length * cos(
                atan2((x1 - x0), (y1 - y0)) - angle)
            path.moveTo(x0, y0)
            path.lineTo(x1, y1)
            path.lineTo(x2, y2)
            path.moveTo(x1, y1)
            path.lineTo(x3, y3)
            painter.drawPath(path)
