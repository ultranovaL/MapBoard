from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GeoObject.Lines.PathItem import PathItem


class HighWayItem(PathItem):
    def __init__(self, line, width=10):
        # 设10dpi=1mm
        super(HighWayItem, self).__init__(line, width)
        self.width = width

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pen1 = QPen(Qt.white, 3, Qt.SolidLine)
        pen1.setCapStyle(Qt.FlatCap)
        pen1.setJoinStyle(Qt.RoundJoin)
        pen2 = QPen(Qt.red, self.width, Qt.SolidLine)
        pen2.setJoinStyle(Qt.RoundJoin)
        pen2.setCapStyle(Qt.FlatCap)
        pen3 = None
        return pen1, pen2, pen3
