from PyQt4 import QtWebKit
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
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
        
        self.browser = QLabel(self)
        vlayout.addWidget(self.browser)
        
        vlayout.addWidget(QuitButton())
        self.setLayout(vlayout)


    def show_browser(self):
        self.browser.setText(self.url_box.text())
