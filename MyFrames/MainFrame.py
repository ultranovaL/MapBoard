from MyFrames.OriginalMainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *
from MyFrames.GeoItemView import GeoItemView


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        # 窗口居中
        self.resize(900, 900)
        self.center()
        # 文件菜单
        self.APP_EXIT.triggered.connect(self.close)
        self.FILE_OPEN.triggered.connect(self.openMsg)
        # 初始化
        self.initData()
        self.initView()

    def initData(self):
        # 初始化数据
        # 变量名前有两个下划线代表类的私有变量
        #    获取QT中的颜色列表(字符串的List)
        self.__colorList = QColor.colorNames()
        self.__GeoItemView = GeoItemView()

    def initView(self):
        '''
        初始化界面
        '''
        # 设置窗体固定尺寸，宽900px,高900px
        # self.setFixedSize(1500,900)
        # 在布局中插入QGraphicsView
        self.drawGridLayout.addWidget(self.__GeoItemView)
        self.__GeoItemView.show()
        # 界面按钮链接函数
        self.button_clear.clicked.connect(self.__GeoItemView.clear)
        self.button_exit.clicked.connect(QCoreApplication.instance().quit)
        # 菜单按钮链接函数
        self.point_sanjiao.triggered.connect(self.__GeoItemView.on_draw_sanjiaodian)
        self.point_tianwendian.triggered.connect(self.__GeoItemView.on_draw_tianwendian)
        self.point_yancong.triggered.connect(self.__GeoItemView.on_draw_yancong)
        self.point_chuyouguan.triggered.connect(self.__GeoItemView.on_draw_chuyouguan)
        self.point_guta.triggered.connect(self.__GeoItemView.on_draw_guta)
        self.point_fadian.triggered.connect(self.__GeoItemView.on_draw_fadian)

        self.line_highway.triggered.connect(self.__GeoItemView.on_draw_highway)
        self.line_buildinghighway.triggered.connect(self.__GeoItemView.on_draw_buildinghighway)
        self.line_buildingprovincialroad.triggered.connect(self.__GeoItemView.on_draw_buildingprovincialroad)
        self.line_xianroad.triggered.connect(self.__GeoItemView.on_draw_xianroad)
        self.line_airplane.triggered.connect(self.__GeoItemView.on_draw_airplane)
        self.line_milestone.triggered.connect(self.__GeoItemView.on_draw_milestone)

        self.Node_Edit.triggered.connect(self.__GeoItemView.on_edit_node)
        self.Item_Move.triggered.connect(self.__GeoItemView.on_move_item)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, '打开', 'C:/', 'All Files(*);;Text Files(*.txt)')
        self.statusbar.showMessage(file)

    # 窗口居中
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
