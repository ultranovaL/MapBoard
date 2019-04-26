from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *


class PathItem(QGraphicsPathItem):
    def __init__(self, line, width=10):
        QGraphicsPathItem.__init__(self)
        self.setFlags(
            QGraphicsPathItem.ItemIsSelectable | QGraphicsPathItem.ItemIsFocusable)
        self.line = line  # 包含定义线要素的QPointF的列表
        self.path = QPainterPath()
        self.cal_path()
        self.width = width  # 线状符号的宽度

    def shape(self):
        stroke = QPainterPathStroker()
        stroke.setWidth(self.width * 2)
        return stroke.createStroke(self.path)

    def cal_path(self):
        if self.line is not None:
            for i in range(len(self.line)):
                if i == 0:
                    # self.path.moveTo(self.line[i].x(), self.line[i].y())
                    self.path.moveTo(self.line[i])
                else:
                    self.path.lineTo(self.line[i])

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget):
        pen1, pen2, pen3 = self.define_pen()
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.draw_line(painter, pen3, pen2, pen1)

    def draw_line(self, painter, *pens):
        # 按照画笔传入顺序绘制，先绘制的在底层，后面依次叠甲覆盖
        for pen in pens:
            if pen is not None:
                painter.setPen(pen)
                painter.drawPath(self.path)

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pass

    def setPath(self, path: QPainterPath):
        self.path = path
        new_line = []
        for i in range(self.path.elementCount()):
            x = self.path.elementAt(i).x
            y = self.path.elementAt(i).y
            new_line.append(QPointF(x, y))
        self.line = new_line.copy()

    def setLine(self, line):
        self.line = line.copy()

    def get_path(self):
        return self.path
