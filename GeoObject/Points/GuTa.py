from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GeoObject.Points.PointItem import PointItem


class Guta(PointItem):
    def __init__(self, x, y):
        super(Guta, self).__init__(x, y)
        self.size = 180
        self.triangle_points = [QPointF(x, y - self.size), QPointF(x - self.size / 6, y), QPointF(x + self.size / 6, y)]

    def boundingRect(self):
        return QRectF(self.x - self.size / 3, self.y - self.size, 2 * self.size / 3, self.size)

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
        path.moveTo(self.x - 5 * self.size / 18, self.y - self.size / 3)
        path.lineTo(self.x + 5 * self.size / 18, self.y - self.size / 3)
        path.moveTo(self.x - 4 * self.size / 18, self.y - 2 * self.size / 3)
        path.lineTo(self.x + 4 * self.size / 18, self.y - 2 * self.size / 3)
        painter.drawPath(path)

