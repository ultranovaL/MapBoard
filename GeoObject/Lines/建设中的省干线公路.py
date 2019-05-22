from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GeoObject.Lines.PathItem import PathItem


class BuildingProvincialRoadItem(PathItem):
    def __init__(self, line, width=6):
        # 设10dpi=1mm
        super(BuildingProvincialRoadItem, self).__init__(line, width)
        self.width = width
        self.dash_len = 8 * 10 / self.width
        self.void_len = 1 * 10 / self.width

    def define_pen(self):
        '''
        定义各种线型，返回三层画笔，第二、三层可为空
        '''
        pen1 = QPen(QColor(185, 131, 33), 4)
        # 自定义dashline的间隔与线划宽度有关
        pen1.setStyle(Qt.CustomDashLine)
        pen1.setDashPattern([self.dash_len * 6 / 4, self.void_len * 6 / 4])
        pen1.setCapStyle(Qt.FlatCap)
        pen1.setJoinStyle(Qt.RoundJoin)

        pen2 = QPen(Qt.black, self.width)
        pen2.setStyle(Qt.CustomDashLine)
        pen2.setDashPattern([self.dash_len, self.void_len])
        pen2.setJoinStyle(Qt.RoundJoin)
        pen2.setCapStyle(Qt.FlatCap)

        pen3 = None
        return pen1, pen2, pen3
