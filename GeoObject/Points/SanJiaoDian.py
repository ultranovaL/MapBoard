from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
from GeoObject.Points.PointItem import PointItem


class SanJiaoDian(PointItem):
    def __init__(self, x, y):
        super(SanJiaoDian, self).__init__(x, y)
        self.size = 160

    def boundingRect(self):
        return QRectF(self.x - self.size / 2, self.y - self.size * 3 ** 0.5 / 3, self.size, self.size)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing, True)
        # 0.1mm=1dpi
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.black))
        circle_coefficients = self.cal_circle(self.x, self.y, 1.5 * self.size / 16)
        painter.drawEllipse(*circle_coefficients)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush())
        path.moveTo(self.x, self.y - self.size / sqrt(3))
        path.lineTo(self.x - self.size / 2, self.y + self.size / 2 / sqrt(3))
        path.lineTo(self.x + self.size / 2, self.y + self.size / 2 / sqrt(3))
        path.lineTo(self.x, self.y - self.size / sqrt(3))
        painter.drawPath(path)
