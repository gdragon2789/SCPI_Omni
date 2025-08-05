from PySide6.QtWidgets import QApplication
from mainApp import MyApp
import sys


def main():
    try:
        app = QApplication(sys.argv)

        # Init GUI
        window = MyApp()
        window.show()
        exit_code = app.exec()
        sys.exit(exit_code)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
