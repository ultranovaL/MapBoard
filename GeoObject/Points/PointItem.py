from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PointItem(QGraphicsItem):
    def __init__(self, x, y):
        QGraphicsItem.__init__(self)
        self.x = x
        self.y = y
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRectF(self.x - 20, self.y - 20, 40, 40)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        pass


