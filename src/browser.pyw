from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt4.QtCore import SIGNAL, QUrl

from quit_button import QuitButton

class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        vlayout = QVBoxLayout()
        
        url_bar = QHBoxLayout()

        self.url_box = QLineEdit()
        self.connect(self.url_box, SIGNAL('returnPressed()'), self.show_browser)
        
        go = QPushButton(self)
        go.setText("Go")
        self.connect(go, SIGNAL('clicked()'), self.show_browser)
        
        url_bar.addWidget(self.url_box)
        url_bar.addWidget(go)
        vlayout.addLayout(url_bar)
        
        javascript_bar = QHBoxLayout()

        self.javascript_box = QLineEdit()
        self.connect(self.javascript_box, SIGNAL('returnPressed()'), self.send_javascript)
        
        ex = QPushButton(self)
        ex.setText("Execute on page")
        self.connect(ex, SIGNAL('clicked()'), self.send_javascript)
        
        javascript_bar.addWidget(self.javascript_box)
        javascript_bar.addWidget(ex)
        vlayout.addLayout(javascript_bar)

        self.browser = QWebView(self)
        vlayout.addWidget(self.browser)
        
        vlayout.addWidget(QuitButton())
        self.setLayout(vlayout)


    def show_browser(self):
        url = QUrl(self.url_box.text())
        self.browser.load(url)
        
    def send_javascript(self):
        self.browser.page().currentFrame().evaluateJavaScript(self.javascript_box.text())
