import sys
from PyQt5.QtWidgets import *
from MyFrames.MainFrame import MainWindow


def start():
    app = QApplication(sys.argv)
    myMainWin = MainWindow()
    myMainWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
