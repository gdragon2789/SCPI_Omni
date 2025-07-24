from PySide6.QtWidgets import QApplication, QWidget
from Config.mainApp import Ui_Application  # This is the generated class
from PySide6.QtCore import Qt,Slot,Signal


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Application()
        self.ui.setupUi(self)  # Setup the UI on this QWidget
        self.connect_signals()

        self.ui.progressBar.setValue(50)
        self.ui.textDisplay.setText("Hello World")
        self.ui.readSeriesNumber.setText("123456789")


    def clear_infor(self):
        self.ui.progressBar.setValue(0)
        self.ui.textDisplay.clear()
        self.ui.readSeriesNumber.clear()

    def connect_signals(self):
        self.ui.progressBar.adjustSize()
        self.ui.selectButton.clicked.connect(self.select_button_clicked)
        self.ui.resetButton.clicked.connect(self.clear_infor)
        self.ui.button_num1.clicked.connect(self.button_yes_clicked)
        self.ui.button_num2.clicked.connect(self.button_no_clicked)

    @Slot()
    def select_button_clicked(self):
        print("select_button_clicked")

    @Slot()
    def reset_button_clicked(self):
        print("reset_button_clicked")

    @Slot()
    def button_yes_clicked(self):
        print("button_yes_clicked")

    @Slot()
    def button_no_clicked(self):
        print("button_no_clicked")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
