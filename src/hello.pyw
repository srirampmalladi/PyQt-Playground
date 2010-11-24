import sys
from PyQt4.QtGui import QApplication, QMainWindow

from quit_button import QuitButton
from menu_bar import MenuBar

app = QApplication(sys.argv)

main_window = QMainWindow()
main_window.resize(160, 60)
main_window.setWindowTitle("O Hai")

QuitButton(main_window)
MenuBar(main_window)

main_window.show()
app.exec_()

