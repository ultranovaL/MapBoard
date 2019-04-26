from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GeoObject.Points.PointItem import PointItem


class ChuYouGuan(PointItem):
    def __init__(self, x, y):
        super(ChuYouGuan, self).__init__(x, y)
        self.r = 60

    def boundingRect(self):
        return QRectF(self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.black))
        circle = self.cal_circle(self.x, self.y, self.r)
        painter.drawEllipse(*circle)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.white))
        painter.drawPie(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2, 0, -180 * 16)
