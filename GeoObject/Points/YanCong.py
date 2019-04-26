from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
from GeoObject.Points.PointItem import PointItem


class YanCong(PointItem):
    def __init__(self, x, y):
        super(YanCong, self).__init__(x, y)
        self.size = 150
        self.triangle_points = [QPointF(x, y - self.size), QPointF(x - 2 * self.size / 15, y),
                                QPointF(x + 2 * self.size / 15, y)]

    def boundingRect(self):
        return QRectF(self.x - self.size / 3, self.y - 4 * self.size / 3, 2 * self.size / 3, 4 * self.size / 3)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.black))
        painter.drawPolygon(QPolygonF(self.triangle_points))
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush())
        path.moveTo(self.x - self.size / 3, self.y)
        path.lineTo(self.x + self.size / 3, self.y)
        path.moveTo(self.x, self.y - self.size)
        path.lineTo(self.x + self.size / 3, self.y - self.size - self.size / 3 * tan(20 * pi / 180))
        painter.drawPath(path)
