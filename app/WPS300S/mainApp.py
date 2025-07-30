from PySide6.QtWidgets import QApplication, QWidget
from app.WPS300S.gui.WPS300S_interface import Ui_MainApp  # This is the generated class
from backend.backend import WPS300S

class MyApp(QWidget):
    def __init__(self, device=None):
        super().__init__()
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)  # Setup the UI on this QWidget
        self.device = device
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
