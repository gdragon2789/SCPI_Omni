from PySide6.QtWidgets import QApplication, QWidget
from gui.WPS300S_interface import Ui_MainApp  # This is the generated class

class MyApp(QWidget):
    def __init__(self, device=None):
        super().__init__()
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)  # Setup the UI on this QWidget
        self.device = device
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def display_set_value(self):
        setup = self.device.get_setup()
        self.ui.setupVoltageDisplay.display(setup[0])
        self.ui.setupCurrentDisplay.display(setup[1])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
