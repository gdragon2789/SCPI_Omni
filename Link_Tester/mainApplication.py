from PySide6.QtWidgets import QApplication, QWidget
from Config.mainApp import Ui_Application  # This is the generated class

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Application()
        self.ui.setupUi(self)  # Setup the UI on this QWidget

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
