from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
from GeoObject.Points.PointItem import PointItem


class TianWenDian(PointItem):
    def __init__(self, x, y):
        super(TianWenDian, self).__init__(x, y)
        self.size = 200
        self.R = self.size / 2
        self.rad = pi / 180
        self.r = self.R * sin(18 * self.rad) / cos(36 * self.rad)
        self.coord = []

    def boundingRect(self):
        return QRectF(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing, True)
        # 绘制中心圆点
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.black))
        circle_coefficients = self.cal_circle(self.x, self.y, 1.5 * self.size / 20)
        painter.drawEllipse(circle_coefficients[0], circle_coefficients[1], circle_coefficients[2],
                            circle_coefficients[-1])
        # 绘制五角星边界
        for i in range(0, 5):
            (x1, y1) = (
                self.x - (self.R * cos((90 + i * 72 + 180) * self.rad)),
                self.y + (self.R * sin((90 + i * 72 + 180) * self.rad)))
            (x2, y2) = (
                self.x - (self.r * cos((90 + 36 + i * 72 + 180) * self.rad)),
                self.y + (self.r * sin((90 + 36 + i * 72 + 180) * self.rad))
            )
            self.coord.append((x1, y1))
            self.coord.append((x2, y2))
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush())
        for point in self.coord:
            if self.coord.index(point) == 0:
                path.moveTo(*point)
            else:
                path.lineTo(*point)
        path.lineTo(*self.coord[0])
        painter.drawPath(path)
