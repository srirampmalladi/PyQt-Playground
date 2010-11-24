from PyQt4 import QtWebKit
from PyQt4.QtGui import QWidget, QVBoxLayout

from quit_button import QuitButton

class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout()
        layout.addStretch(1)
        
        layout.addWidget(QuitButton())
        self.setLayout(layout)
        