import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QMessageBox 

from quit_confirm import QuitConfirm
from browser import BrowserWidget

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.add_file_menu()
        self.add_help_menu()
        self.resize(160, 60)
        self.setWindowTitle("O Hai")

        self.setCentralWidget(BrowserWidget(self))
        

    def add_file_menu(self):
        file_menu = self.menuBar().addMenu('File')
        
        exit = QAction('Quit', self)
        self.connect(exit, SIGNAL('triggered()'), self.quit)

        file_menu.addAction(exit)
    
    
    def add_help_menu(self):
        help_menu = self.menuBar().addMenu('Help')
        
        about = QAction('About', self)
        self.connect(about, SIGNAL('triggered()'), self.show_about_dialog)

        help_menu.addAction(about)
    
    
    def show_about_dialog(self):
        about_dialog = QMessageBox(self)
        about_dialog.setWindowTitle("About")
        about_dialog.setText("Sean O'Malley did this.")
        about_dialog.setStandardButtons(QMessageBox.Ok)
        about_dialog.setDefaultButton(QMessageBox.Ok)
        about_dialog.exec_()

    
    def quit(self, event=None):
        QuitConfirm(self.parent()).display()


app = QApplication(sys.argv)

main_window = MainWindow()

main_window.show()
app.exec_()

