# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OriginalMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 403)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.drawGridLayout = QtWidgets.QGridLayout()
        self.drawGridLayout.setObjectName("drawGridLayout")
        self.gridLayout.addLayout(self.drawGridLayout, 0, 0, 1, 2)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 2, 0, 1, 1)
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setObjectName("button_exit")
        self.gridLayout.addWidget(self.button_exit, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 18))
        self.menubar.setObjectName("menubar")
        self.POINT_MENU = QtWidgets.QMenu(self.menubar)
        self.POINT_MENU.setObjectName("POINT_MENU")
        self.LINE_MENU = QtWidgets.QMenu(self.menubar)
        self.LINE_MENU.setObjectName("LINE_MENU")
        self.POLYGON_MENU = QtWidgets.QMenu(self.menubar)
        self.POLYGON_MENU.setObjectName("POLYGON_MENU")
        self.FILE_MENU = QtWidgets.QMenu(self.menubar)
        self.FILE_MENU.setObjectName("FILE_MENU")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.FILE_NEW = QtWidgets.QAction(MainWindow)
        self.FILE_NEW.setObjectName("FILE_NEW")
        self.FILE_OPEN = QtWidgets.QAction(MainWindow)
        self.FILE_OPEN.setObjectName("FILE_OPEN")
        self.FILE_SAVE = QtWidgets.QAction(MainWindow)
        self.FILE_SAVE.setObjectName("FILE_SAVE")
        self.FILE_SAVE_AS = QtWidgets.QAction(MainWindow)
        self.FILE_SAVE_AS.setObjectName("FILE_SAVE_AS")
        self.FILE_MRU_FILE10 = QtWidgets.QAction(MainWindow)
        self.FILE_MRU_FILE10.setObjectName("FILE_MRU_FILE10")
        self.point_sanjiao = QtWidgets.QAction(MainWindow)
        self.point_sanjiao.setObjectName("point_sanjiao")
        self.APP_EXIT = QtWidgets.QAction(MainWindow)
        self.APP_EXIT.setObjectName("APP_EXIT")
        self.line_buildinghighway = QtWidgets.QAction(MainWindow)
        self.line_buildinghighway.setObjectName("line_buildinghighway")
        self.line_highway = QtWidgets.QAction(MainWindow)
        self.line_highway.setObjectName("line_highway")
        self.Node_Edit = QtWidgets.QAction(MainWindow)
        self.Node_Edit.setObjectName("Node_Edit")
        self.Item_Move = QtWidgets.QAction(MainWindow)
        self.Item_Move.setObjectName("Item_Move")
        self.line_buildingprovincialroad = QtWidgets.QAction(MainWindow)
        self.line_buildingprovincialroad.setObjectName("line_buildingprovincialroad")
        self.line_xianroad = QtWidgets.QAction(MainWindow)
        self.line_xianroad.setObjectName("line_xianroad")
        self.line_airplane = QtWidgets.QAction(MainWindow)
        self.line_airplane.setObjectName("line_airplane")
        self.line_milestone = QtWidgets.QAction(MainWindow)
        self.line_milestone.setObjectName("line_milestone")
        self.point_chuyouguan = QtWidgets.QAction(MainWindow)
        self.point_chuyouguan.setObjectName("point_chuyouguan")
        self.point_guta = QtWidgets.QAction(MainWindow)
        self.point_guta.setObjectName("point_guta")
        self.point_fadian = QtWidgets.QAction(MainWindow)
        self.point_fadian.setObjectName("point_fadian")
        self.point_tianwendian = QtWidgets.QAction(MainWindow)
        self.point_tianwendian.setObjectName("point_tianwendian")
        self.point_yancong = QtWidgets.QAction(MainWindow)
        self.point_yancong.setObjectName("point_yancong")
        self.POINT_MENU.addAction(self.point_sanjiao)
        self.POINT_MENU.addAction(self.point_tianwendian)
        self.POINT_MENU.addAction(self.point_yancong)
        self.POINT_MENU.addAction(self.point_chuyouguan)
        self.POINT_MENU.addAction(self.point_guta)
        self.POINT_MENU.addAction(self.point_fadian)
        self.LINE_MENU.addAction(self.line_highway)
        self.LINE_MENU.addAction(self.line_buildinghighway)
        self.LINE_MENU.addAction(self.line_buildingprovincialroad)
        self.LINE_MENU.addAction(self.line_xianroad)
        self.LINE_MENU.addAction(self.line_airplane)
        self.LINE_MENU.addAction(self.line_milestone)
        self.FILE_MENU.addAction(self.FILE_NEW)
        self.FILE_MENU.addAction(self.FILE_OPEN)
        self.FILE_MENU.addAction(self.FILE_SAVE)
        self.FILE_MENU.addAction(self.FILE_SAVE_AS)
        self.FILE_MENU.addSeparator()
        self.FILE_MENU.addAction(self.FILE_MRU_FILE10)
        self.FILE_MENU.addSeparator()
        self.FILE_MENU.addAction(self.APP_EXIT)
        self.menubar.addAction(self.FILE_MENU.menuAction())
        self.menubar.addAction(self.POINT_MENU.menuAction())
        self.menubar.addAction(self.LINE_MENU.menuAction())
        self.menubar.addAction(self.POLYGON_MENU.menuAction())
        self.toolBar.addAction(self.line_buildinghighway)
        self.toolBar.addAction(self.line_highway)
        self.toolBar.addAction(self.Node_Edit)
        self.toolBar.addAction(self.Item_Move)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易绘图系统"))
        self.button_clear.setText(_translate("MainWindow", "清空画板"))
        self.button_exit.setText(_translate("MainWindow", "退出"))
        self.POINT_MENU.setTitle(_translate("MainWindow", "点状符号"))
        self.LINE_MENU.setTitle(_translate("MainWindow", "线状符号"))
        self.POLYGON_MENU.setTitle(_translate("MainWindow", "面"))
        self.FILE_MENU.setTitle(_translate("MainWindow", "文件"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.FILE_NEW.setText(_translate("MainWindow", "新建"))
        self.FILE_OPEN.setText(_translate("MainWindow", "打开"))
        self.FILE_SAVE.setText(_translate("MainWindow", "保存"))
        self.FILE_SAVE_AS.setText(_translate("MainWindow", "另存为"))
        self.FILE_MRU_FILE10.setText(_translate("MainWindow", "最近的文件"))
        self.point_sanjiao.setText(_translate("MainWindow", "三角点"))
        self.point_sanjiao.setToolTip(_translate("MainWindow", "三角点"))
        self.APP_EXIT.setText(_translate("MainWindow", "退出"))
        self.line_buildinghighway.setText(_translate("MainWindow", "建筑中的高速公路"))
        self.line_highway.setText(_translate("MainWindow", "高速公路"))
        self.Node_Edit.setText(_translate("MainWindow", "节点编辑"))
        self.Item_Move.setText(_translate("MainWindow", "移动"))
        self.line_buildingprovincialroad.setText(_translate("MainWindow", "建筑中的省干线公路"))
        self.line_xianroad.setText(_translate("MainWindow", "县乡公路"))
        self.line_airplane.setText(_translate("MainWindow", "能起降飞机的公路段"))
        self.line_milestone.setText(_translate("MainWindow", "公路里程起止符号"))
        self.point_chuyouguan.setText(_translate("MainWindow", "储油罐"))
        self.point_guta.setText(_translate("MainWindow", "古塔"))
        self.point_fadian.setText(_translate("MainWindow", "发电厂"))
        self.point_tianwendian.setText(_translate("MainWindow", "独立天文点"))
        self.point_yancong.setText(_translate("MainWindow", "烟囱"))

