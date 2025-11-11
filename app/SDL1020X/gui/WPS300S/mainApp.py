from PySide6.QtWidgets import QApplication, QWidget
from WPS300S_interface import Ui_MainApp  # This is the generated class
from PySide6.QtCore import Qt,Slot,Signal


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)  # Setup the UI on this QWidget


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
