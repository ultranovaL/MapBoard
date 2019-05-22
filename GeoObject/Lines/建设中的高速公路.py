from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GeoObject.Lines.PathItem import PathItem


class BuildingHighWayItem(PathItem):
    def __init__(self, line, width=10):
        # 设10dpi=1mm
        super(BuildingHighWayItem, self).__init__(line, width=10)
        self.width = width

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pen1 = QPen(Qt.white, 3)
        # 自定义dashline时间隔与线划宽度有关
        pen1.setStyle(Qt.CustomDashLine)
        pen1.setDashPattern([8 * 10 / 3, 1 * 10 / 3])
        pen1.setCapStyle(Qt.FlatCap)
        pen1.setJoinStyle(Qt.RoundJoin)

        pen2 = QPen(Qt.red, self.width)
        pen2.setStyle(Qt.CustomDashLine)
        pen2.setDashPattern([8, 1])
        pen2.setJoinStyle(Qt.RoundJoin)
        pen2.setCapStyle(Qt.FlatCap)

        pen3 = None
        return pen1, pen2, pen3
