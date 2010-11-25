from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt4.QtCore import SIGNAL, QUrl

from quit_button import QuitButton

class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        vlayout = QVBoxLayout()
        
        hlayout = QHBoxLayout()

        self.url_box = QLineEdit()
        go = QPushButton(self)
        go.setText("go")
        self.connect(go, SIGNAL('clicked()'), self.show_browser)
        
        hlayout.addWidget(self.url_box)
        hlayout.addWidget(go)
        vlayout.addLayout(hlayout)
        
        self.browser = QWebView(self)
        vlayout.addWidget(self.browser)
        
        vlayout.addWidget(QuitButton())
        self.setLayout(vlayout)


    def show_browser(self):
        url = QUrl(self.url_box.text())
        self.browser.load(url)
        
