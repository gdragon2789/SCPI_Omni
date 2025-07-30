import sys
from PySide6.QtWidgets import QApplication
from mainApp import MyApp
from backend.backend import WPS300S
import time
import os
import sys

# Lấy thư mục hiện tại của file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Lên 2 cấp để đến thư mục SCPI_Omni
parent_dir = os.path.abspath(os.path.join(current_dir,".." ,".."))
# Thêm vào sys.path nếu chưa có
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from api.__init__ import *



def main():
    scanner = PyVISAScanner()
    # scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="WPS300S-15005")
    # Init SCPI communication
    wps300s = WPS300S(visa_port=port, connection_type=connect_type)

    app = QApplication(sys.argv)

    # Init GUI
    window = MyApp(device=wps300s)
    window.show()

    exit_code = app.exec()
    wps300s.close()  # Cleanup
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
