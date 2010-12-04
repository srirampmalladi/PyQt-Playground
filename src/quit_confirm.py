from PyQt4.QtGui import QMessageBox, qApp

class QuitConfirm(QMessageBox):
    def __init__(self, parent=None):
        QMessageBox.__init__(self, parent)
        self.setWindowTitle("Quitting")
        self.setText("For reals?")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.Yes)

    def display(self):
        self.process_return_code(self.exec_())
        
    def process_return_code(self, ret):
        if ret == QMessageBox.Yes:
            qApp.quit()
        elif ret == QMessageBox.No:
            pass
