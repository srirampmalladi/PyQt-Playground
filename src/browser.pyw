from PyQt4 import QtWebKit
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt4.QtCore import SIGNAL

from quit_button import QuitButton

class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        
        hlayout = QHBoxLayout()
        
        self.url_box = QLineEdit()
        go = QPushButton(self)
        go.setText("go")
        self.connect(go, SIGNAL('clicked()'), self.show_browser)
        
        hlayout.addWidget(self.url_box)
        hlayout.addWidget(go)
        
        vlayout.addLayout(hlayout)
        vlayout.addWidget(QuitButton())
        self.setLayout(vlayout)

    def show_browser(self):
        dummy_dialog = QMessageBox(self)
        dummy_dialog.setWindowTitle("Browser")
        dummy_dialog.setText(self.url_box.text())
        dummy_dialog.setStandardButtons(QMessageBox.Ok)
        dummy_dialog.setDefaultButton(QMessageBox.Ok)
        dummy_dialog.exec_()