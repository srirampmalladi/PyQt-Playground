from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QPushButton
from quit_confirm import QuitConfirm

class QuitButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setText("Bye")
        self.setToolTip("Quit")
        self.connect(self, SIGNAL('clicked()'), self.clicked)

    def clicked(self):
        QuitConfirm(self.parent()).display()