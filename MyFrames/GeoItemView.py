from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GeoObject.Type import OperationType, PointType, LineType
# 点状符号
from GeoObject.Points.三角点 import SanJiaoDian
from GeoObject.Points.独立天文点 import TianWenDian
from GeoObject.Points.古塔 import Guta
from GeoObject.Points.储油罐 import ChuYouGuan
from GeoObject.Points.烟囱 import YanCong
from GeoObject.Points.发电厂 import FaDianChang
# 线状符号
from GeoObject.Lines.高速公路 import HighWayItem
from GeoObject.Lines.建设中的省干线公路 import BuildingProvincialRoadItem
from GeoObject.Lines.建设中的高速公路 import BuildingHighWayItem
from GeoObject.Lines.县级公路 import XianRoadItem
from GeoObject.Lines.能起降分级的公路路段 import PlaneRoadItem
from GeoObject.Lines.公路里程起止点 import MileageRoadItem


class GeoItemView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.__init_view()
        self.__init_data()
        self.setMouseTracking(True)  # 设置跟踪鼠标

    def __init_data(self):
        self.isDrawing = False  # 绘图进行与否的标志
        self.push_numb = 1  # 设置鼠标为第一次摁下
        self.movePoint = QPointF()  # item移动的过程点
        self.origPoint = QPointF()  # item移动时的起始点
        self.flag = LineType.HighWay  # item类型
        self.isEditing = False  # 是否正在编辑节点
        self.isMoving = False
        self.currentState = OperationType.DrawType
        self.editPointIndex = -1  # 正在编辑的节点的序号
        # 画点函数字典
        self.point_fun = {
            PointType.SanJiaoDian: SanJiaoDian,
            PointType.TianWenDian: TianWenDian,
            PointType.GuTa: Guta,
            PointType.FaDianChang: FaDianChang,
            PointType.YanCong: YanCong,
            PointType.YouGuan: ChuYouGuan
        }
        self.point_item_show = self.point_fun[PointType.SanJiaoDian](0, 0)
        # 画线函数字典
        self.road_fun = {
            LineType.HighWay: HighWayItem,
            LineType.BuildingHighWay: BuildingHighWayItem,
            LineType.BuildingProvincialHighWay: BuildingProvincialRoadItem,
            LineType.XianRoad: XianRoadItem,
            LineType.PlaneRoad: PlaneRoadItem,
            LineType.MileageRoad: MileageRoadItem
        }
        self.line_item_show = self.road_fun[self.flag](line=None)
        self.isLine = False  # 判断当前绘制的是直线还是点状符号
        self.line = []
        self.points = []  # 点集
        self.shapes = []  # item集合
        self.temp_shapes = []  # 临时item集合
        self.cur_selected_item = 0

    def __init_view(self):
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 保证scene与view的左边、顶对齐，从而保证坐标一致性
        self.my_scene = QGraphicsScene()
        self.my_scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(self.my_scene)

    def mousePressEvent(self, event: QMouseEvent):
        if self.currentState == OperationType.DrawType:
            self.mouse_press_draw(event)
        elif self.currentState == OperationType.MoveType:
            self.mouse_press_move(event)
        elif self.currentState == OperationType.EditType:
            self.mouse_press_edit(event)
        try:
            self.cur_selected_item = self.my_scene.itemAt(event.pos(), self.my_scene.items()[0].transform())
        except:
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.currentState == OperationType.DrawType:
            self.mouse_move_draw(event)
        elif self.currentState == OperationType.MoveType:
            self.mouse_move_move(event)
        elif self.currentState == OperationType.EditType:
            self.mouse_move_edit(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.currentState == OperationType.DrawType:
            self.mouse_release_draw(event)
        elif self.currentState == OperationType.MoveType:
            self.mouse_release_move(event)
        elif self.currentState == OperationType.EditType:
            self.mouse_release_edit(event)

    def mouse_press_draw(self, event):
        if self.isLine:
            if event.button() == Qt.LeftButton & self.isDrawing:
                if self.push_numb == 1:
                    self.line_item_show = None
                    self.line.append(event.pos())
                    self.push_numb = -1
                else:
                    self.my_scene.removeItem(self.line_item_show)
                    current_point = event.pos()
                    self.line.append(current_point)
                    self.show_item()
            elif event.button() == Qt.RightButton and self.isDrawing:
                line = self.line.copy()
                line_item_to_shapes = self.road_fun[self.flag](line)
                self.shapes.append(line_item_to_shapes)
                self.show_shape(self.shapes)
                self.line.clear()
                self.isDrawing = False
                self.push_numb = 1
        if self.isLine is False:
            if event.button() == Qt.LeftButton and self.isDrawing:
                x = event.pos().x()
                y = event.pos().y()
                self.show_item(x, y)
                point_to_shapes = self.point_item_show
                self.shapes.append(point_to_shapes)
            elif event.button() == Qt.RightButton and self.isDrawing:
                self.isDrawing = False

    def mouse_press_move(self, event):
        if len(self.my_scene.items()) > 0 and event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.cur_selected_item = self.my_scene.itemAt(event.pos(), self.my_scene.items()[0].transform())
            self.isMoving = True
            if self.cur_selected_item:
                self.my_scene.clearSelection()
                self.origPoint = event.pos()
                self.cur_selected_item.setSelected(True)
        elif event.button() == Qt.RightButton:
            self.setCursor(Qt.ArrowCursor)

    def mouse_press_edit(self, event):
        try:
            if event.button() == Qt.LeftButton and self.isEditing:
                press_point = event.pos()
                for point in self.points:
                    if abs(press_point.x() - point.x()) < 5 and abs(press_point.y() - point.y()) < 5:
                        newpoint_circle = QGraphicsEllipseItem(point.x() - 5, point.y() - 5, 10, 10)
                        newpoint_circle.setBrush(Qt.red)
                        origPointCricle = self.my_scene.itemAt(point, self.my_scene.items()[0].transform())
                        self.temp_shapes.remove(origPointCricle)
                        self.temp_shapes.append(newpoint_circle)
                        self.show_shape(self.temp_shapes)
                        self.editPointIndex = self.points.index(point)
                    else:
                        pass
            if event.button() == Qt.LeftButton and self.editPointIndex == -1 and len(
                    self.my_scene.items()) > 0 and self.isEditing is False:  # 若之前没有编辑，则单击开始编辑
                self.setMouseTracking(False)
                self.points.clear()
                self.curEditItem = self.my_scene.itemAt(event.pos(), self.my_scene.items()[0].transform())
                self.temp_shapes = self.shapes.copy()
                cur_edit_line: QGraphicsPathItem = self.curEditItem
                self.show_edit_point(cur_edit_line)
                self.isEditing = True
            elif event.button() == Qt.RightButton and self.isEditing:
                self.setMouseTracking(True)
                self.isEditing = False
                self.show_shape(self.shapes)
                self.points.clear()
                self.temp_shapes.clear()
                self.curEditItem = None
                self.editPointIndex = -1
        except:
            pass

    def mouse_move_draw(self, event):
        if self.isDrawing and self.push_numb != 1:
            if self.isLine is False:
                pass
            elif self.isLine is True:
                tmp_points = self.line.copy()
                tmp_points.append(event.pos())
                tmp_line = self.road_fun[self.flag](tmp_points)
                self.temp_shapes = self.shapes.copy()
                self.temp_shapes.append(tmp_line)
                self.show_shape(self.temp_shapes)

    def mouse_move_move(self, event):
        if self.isMoving:
            self.movePoint = event.pos()
            move_point = self.movePoint
            dx = move_point.x() - self.origPoint.x()
            dy = move_point.y() - self.origPoint.y()
            for item in self.my_scene.selectedItems():
                item.moveBy(dx, dy)
            self.origPoint = move_point

    def mouse_move_edit(self, event):
        if self.isEditing:
            self.movePoint = event.pos()
            self.points[self.editPointIndex] = event.pos()
            cur_edit_line = self.curEditItem
            if cur_edit_line is not None:
                cur_points = self.points.copy()
                tmp_path = QPainterPath(self.points[0])
                for i in range(len(self.points)):
                    tmp_path.lineTo(self.points[i])
                cur_edit_line.setPath(tmp_path)
                # cur_edit_line.setLine(cur_points)

            temp_shapes = self.shapes.copy()
            for point in self.points:  # 移动中画节点
                if self.points.index(point) == self.editPointIndex:
                    point_circle = QGraphicsEllipseItem(point.x() - 5, point.y() - 5, 10, 10)
                    point_circle.setBrush(Qt.red)
                    temp_shapes.append(point_circle)
                else:
                    point_circle = QGraphicsEllipseItem(point.x() - 5, point.y() - 5, 10, 10)
                    point_circle.setBrush(Qt.blue)
                    temp_shapes.append(point_circle)

            self.show_shape(temp_shapes)

    def mouse_release_draw(self, event):
        pass

    def mouse_release_move(self, event):
        self.setCursor(Qt.OpenHandCursor)
        self.my_scene.clearSelection()

    def mouse_release_edit(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.temp_shapes = self.shapes.copy()
        for point in self.points:
            point_circle = QGraphicsEllipseItem(point.x() - 5, point.y() - 5, 10, 10)
            point_circle.setBrush(Qt.blue)
            self.temp_shapes.append(point_circle)
        self.editPointIndex = -1
        self.show_shape(self.temp_shapes)

    def keyPressEvent(self, event: QKeyEvent):
        try:
            if event.key() == Qt.Key_Backspace:
                self.shapes.remove(self.cur_selected_item)
                self.show_shape(self.shapes)
        except:
            pass

    '''
       画板处理/辅助函数
    '''

    def clear(self):
        while len(self.my_scene.items()) > 0:
            self.my_scene.removeItem(self.my_scene.items()[0])
        self.shapes.clear()

    def show_item(self, *point):  # 将item临时展现在屏幕上
        if self.isLine:
            self.line_item_show = self.road_fun[self.flag](line=self.line)
            self.my_scene.addItem(self.line_item_show)
        else:
            self.point_item_show = self.point_fun[self.flag](point[0], point[1])
            self.my_scene.addItem(self.point_item_show)

    def show_shape(self, shapes):  # 用于不断刷新绘制保存在shapes列表中的items
        while len(self.my_scene.items()) > 0:
            self.my_scene.removeItem(self.my_scene.items()[0])
        for shape in shapes:
            self.my_scene.addItem(shape)

    def show_edit_point(self, line_path):  # 显示线要素可编辑节点
        if line_path is not None:
            cur_line_path = line_path.path
            for i in range(cur_line_path.elementCount()):
                cur_point = QPointF(cur_line_path.elementAt(i).x, cur_line_path.elementAt(i).y)
                self.points.append(cur_point)
                point_circle = QGraphicsEllipseItem(cur_point.x() - 5, cur_point.y() - 5, 10, 10)
                point_circle.setBrush(Qt.blue)
                self.temp_shapes.append(point_circle)
            self.show_shape(self.temp_shapes)

    '''
    操作响应函数
    '''

    def on_edit_node(self):
        self.currentState = OperationType.EditType
        self.setCursor(Qt.ArrowCursor)
        self.isDrawing = False
        self.isMoving = False

    def on_move_item(self):
        self.currentState = OperationType.MoveType
        self.setCursor(Qt.OpenHandCursor)
        self.isDrawing = False
        self.isEditing = False

    '''
    点状符号响应函数
    '''

    def on_draw_sanjiaodian(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.SanJiaoDian
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    def on_draw_tianwendian(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.TianWenDian
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    def on_draw_yancong(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.YanCong
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    def on_draw_chuyouguan(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.YouGuan
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    def on_draw_guta(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.GuTa
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    def on_draw_fadian(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = PointType.FaDianChang
        self.isDrawing = True
        self.isLine = False
        self.currentState = OperationType.DrawType

    '''
    线状符号响应函数
    '''

    def on_draw_highway(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.HighWay
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType

    def on_draw_buildinghighway(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.BuildingHighWay
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType

    def on_draw_buildingprovincialroad(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.BuildingProvincialHighWay
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType

    def on_draw_xianroad(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.XianRoad
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType

    def on_draw_airplane(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.PlaneRoad
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType

    def on_draw_milestone(self):
        self.setCursor(Qt.ArrowCursor)
        self.flag = LineType.MileageRoad
        self.isDrawing = True
        self.isLine = True
        self.currentState = OperationType.DrawType
