import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets

class MouseTracker(QtWidgets.QDialog):
    def __init__(self, parent=None, size=256):
        super(MouseTracker, self).__init__(parent)
        self.size = size
        self.initUI()
        self.setMouseTracking(True)
        self.entropy = ''
        self.addNew = True
        self.eventSelector = True

    def initUI(self):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Mouse Tracker')

    def mouseMoveEvent(self, event):
        if len(self.entropy) > (self.size + 1024):
            self.entropy = self.entropy[512:(self.size+512)]
            self.addNew = False
            self.setWindowTitle('100% Done close the window now')
            print('Random {}bit entropy:\n'.format(self.size), self.entropy)
            print('len is:', len(self.entropy))
            window.close()
        else:
            if self.addNew:
                if len(self.entropy) > 1024:
                    self.setWindowTitle(
                        '({} : {}) {}%'.format(
                            event.scenePosition().x(),
                            event.scenePosition().y(),
                            int(((len(self.entropy) - 1024) * 100) / self.size)
                        ))
                else:
                    self.setWindowTitle('move mouse in box randomly')
                if self.eventSelector:
                    self.entropy = self.entropy + bin(int(event.scenePosition().x()))[2:]
                    self.eventSelector = False
                else:
                    self.entropy = self.entropy + bin(int(event.scenePosition().y()))[2:]
                    self.eventSelector = True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 256
    app = QApplication([])
    window = MouseTracker(size=size)
    window.show()
    sys.exit(app.exec())
