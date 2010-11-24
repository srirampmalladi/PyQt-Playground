import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QApplication, QMainWindow, QAction

from quit_button import QuitButton
from quit_confirm import QuitConfirm

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.add_file_menu()
        self.add_help_menu()
        self.resize(160, 60)
        self.setWindowTitle("O Hai")

        self.setCentralWidget(QuitButton(self))
        

    def add_file_menu(self):
        file_menu = self.menuBar().addMenu('File')
        
        exit = QAction('Quit', self)
        self.connect(exit, SIGNAL('triggered()'), self.quit)

        file_menu.addAction(exit)
    
    
    def add_help_menu(self):
        pass
    
    
    def quit(self):
        QuitConfirm(self.parent()).display()

app = QApplication(sys.argv)

main_window = MainWindow()

main_window.show()
app.exec_()

