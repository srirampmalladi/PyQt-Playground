from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt4.QtCore import QObject, SIGNAL, QUrl, pyqtSlot

from quit_button import QuitButton

class WebkitBridge(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    
    @pyqtSlot(str)
    def show_message(self, message):
        box = QMessageBox(self.parent())
        box.setText(message)
        box.setStandardButtons(QMessageBox.Yes)
        box.setWindowTitle("Hai")
        box.exec_()


class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        vlayout = QVBoxLayout()
        
        vlayout.addLayout(self.get_url_bar())
        
        javascript_bar = self.get_javascript_bar()
        vlayout.addLayout(javascript_bar)

        self.browser = QWebView(self)
        self.browser_frame = self.browser.page().currentFrame()
        
        self.connect(self.browser_frame, SIGNAL('javaScriptWindowObjectCleared()'),
                      self.add_javascript_bridge);
        vlayout.addWidget(self.browser)
        
        vlayout.addWidget(QuitButton())
        self.setLayout(vlayout)


    def get_url_bar(self):
        url_bar = QHBoxLayout()
    
        self.url_box = QLineEdit()
        self.connect(self.url_box, SIGNAL('returnPressed()'), self.show_browser)
        
        go = QPushButton(self)
        go.setText("Go")
        self.connect(go, SIGNAL('clicked()'), self.show_browser)
        
        url_bar.addWidget(self.url_box)
        url_bar.addWidget(go)
        return url_bar


    def get_javascript_bar(self):
        javascript_bar = QHBoxLayout()

        self.javascript_box = QLineEdit()
        self.connect(self.javascript_box, SIGNAL('returnPressed()'), self.send_javascript)
        
        ex = QPushButton(self)
        ex.setText("Execute on page")
        self.connect(ex, SIGNAL('clicked()'), self.send_javascript)
        
        javascript_bar.addWidget(self.javascript_box)
        javascript_bar.addWidget(ex)
        return javascript_bar

    def add_javascript_bridge(self):
        self.browser_frame.addToJavaScriptWindowObject("webkitBridge", WebkitBridge())

    def send_javascript(self):
        self.browser.page().currentFrame().evaluateJavaScript(self.javascript_box.text())

    
    def show_browser(self):
        url = QUrl(self.url_box.text())
        self.browser.load(url)
        
