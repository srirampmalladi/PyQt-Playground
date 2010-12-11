from PyQt4.QtGui import QApplication, QMainWindow
import sys

from test import Ui_Dialog
from testmain import Ui_MainWindow
from PyQt4 import QtGui

app = QApplication(sys.argv)
main_window = QMainWindow()
ui_main_window = Ui_MainWindow()
ui_main_window.setupUi(main_window)


main_window.show()
app.exec_()
