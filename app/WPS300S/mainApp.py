from PySide6.QtWidgets import QApplication, QWidget
from gui.WPS300S_interface import Ui_MainApp  # This is the generated class
from PySide6.QtCore import Qt,Slot,Signal,QTimer,QThread
from PySide6.QtWidgets import QMessageBox, QFileDialog
import csv
import datetime
from threads.PollingWorker import PollingWorker
import atexit
from backend.backend import WPS300S
from setup.search_device import *
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis


class MyApp(QWidget):
    def __init__(self, device: WPS300S = None):
        super().__init__()
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)
        self.device = self.search_device()
        self.output_status = False
        self.ui.stackedWidget.setCurrentIndex(0)

        self.csv_file = None
        self.csv_writer = None
        self.logging_enabled = False

        if self.device:
            self.setup_signal()
            self.hire_worker()
            self.draw_graph()

        atexit.register(self.reset)

    def messageBox(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def search_device(self):
        wps300s = None
        timeout = 10  # seconds
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                dev_scan = PyVISAScanner()
                connect_type, port = dev_scan.scan_for_instruments(expected_id="WPS300S-15005")
                wps300s = WPS300S(visa_port=port, connection_type=connect_type)
                print("Device found.")
                break  # success
            except Exception as e:
                print(e)
                print("Device not found yet, retrying...")
                time.sleep(0.5)  # wait before retrying

        if wps300s is None:
            self.messageBox("Timed out", "WPS300S not found.")
            raise Exception(f"Device search timed out after {timeout} seconds.")

        return wps300s

    def hire_worker(self):
        self.poll_thread = QThread()
        self.poll_worker = PollingWorker(self.device)
        self.poll_worker.moveToThread(self.poll_thread)

        self.poll_thread.started.connect(self.poll_worker.start)
        self.poll_worker.data_ready.connect(self.update_display)

        self.poll_thread.start()

    def setup_signal(self):
        self.ui.outPutButton.clicked.connect(self.output_signal)
        self.ui.setupButton.clicked.connect(self.setup_value_signal)
        self.ui.defaultSetupButton.clicked.connect(self.default_value_signal)
        self.ui.basicButton.clicked.connect(self.switch_to_basic)
        self.ui.graphButton.clicked.connect(self.switch_to_graph)
        self.ui.logCSVButton.clicked.connect(self.start_logging_csv)

    @Slot(tuple)
    def update_display(self, data):
        setup, vcm = data
        self.ui.setupVoltageDisplay.display(f"{setup[0]:.3f}")
        self.ui.setupCurrentDisplay.display(f"{setup[1]:.4f}")
        self.ui.outputVoltageDisplay.display(f"{vcm[0]:.3f}")
        self.ui.outputCurrentDisplay.display(f"{vcm[1]:.4f}")

        self.data_counter += 1
        self.series_v.append(self.data_counter, vcm[0])
        self.series_c.append(self.data_counter, vcm[1])

        # Update X range to show last 100 points
        self.axis_x.setRange(max(0, self.data_counter - 100), self.data_counter)

        # Use only last 100 points for performance
        v_points = self.series_v.pointsVector()[-100:]
        c_points = self.series_c.pointsVector()[-100:]

        v_y_values = [p.y() for p in v_points]
        c_y_values = [p.y() for p in c_points]

        if v_y_values:
            vmin = min(v_y_values)
            vmax = max(v_y_values)
            vpad = (vmax - vmin) * 0.1 or 0.1
            self.axis_y_voltage.setRange(vmin - vpad, vmax + vpad)

        if c_y_values:
            cmin = min(c_y_values)
            cmax = max(c_y_values)
            cpad = (cmax - cmin) * 0.1 or 0.1
            self.axis_y_current.setRange(cmin - cpad, cmax + cpad)

        if self.logging_enabled and self.csv_writer:
            now = datetime.datetime.now().isoformat(timespec='seconds')
            self.csv_writer.writerow([now, setup[0], setup[1], vcm[0], vcm[1]])

    def draw_graph(self):
        self.series_v = QLineSeries(name="Voltage")
        self.series_c = QLineSeries(name="Current")
        self.series_v.setUseOpenGL(True)
        self.series_c.setUseOpenGL(True)

        self.chart = QChart()
        self.chart.addSeries(self.series_v)
        self.chart.addSeries(self.series_c)

        # Default X axis
        self.axis_x = QValueAxis()
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series_v.attachAxis(self.axis_x)
        self.series_c.attachAxis(self.axis_x)

        # Left Y axis for voltage
        self.axis_y_voltage = QValueAxis()
        self.axis_y_voltage.setTitleText("Voltage (V)")
        self.chart.addAxis(self.axis_y_voltage, Qt.AlignLeft)
        self.series_v.attachAxis(self.axis_y_voltage)

        # Right Y axis for current
        self.axis_y_current = QValueAxis()
        self.axis_y_current.setTitleText("Current (A)")
        self.chart.addAxis(self.axis_y_current, Qt.AlignRight)
        self.series_c.attachAxis(self.axis_y_current)

        # Set initial axis ranges
        self.axis_y_voltage.setRange(0, 60)
        self.axis_y_current.setRange(0, 1.0)  # Adjusted for better scaling

        self.ui.graphicsViewDisplay.setChart(self.chart)
        self.data_counter = 0

    @Slot()
    def output_signal(self):
        if self.output_status:
            self.device.disable_output()
            self.ui.outPutStatus.setText("OFF")
            self.output_status = False
            res = self.device.get_output()
            print(res)

        else:
            self.device.enable_output()
            self.ui.outPutStatus.setText("ON")
            self.output_status = True
            res = self.device.get_output()
            print(res)


    @Slot()
    def setup_value_signal(self):
        setup_voltage = self.ui.setupVoltageInput.text()
        setup_current = self.ui.setupCurrentInput.text()
        self.device.setup(setup_voltage, setup_current)

    @Slot()
    def default_value_signal(self):
        volt = 5.0
        curr = 1.0
        self.device.setup(volt=volt, curr=curr)

    @Slot()
    def switch_to_graph(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def switch_to_basic(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def reset(self):
        self.default_value_signal()
        self.device.disable_output()
        self.device.close()
        if self.csv_file:
            self.csv_file.close()

    def start_logging_csv(self):
        if not self.logging_enabled:
            path, _ = QFileDialog.getSaveFileName(
                self,
                "Save CSV Log",
                "log.csv",
                "CSV Files (*.csv)"
            )
            if path:
                try:
                    self.csv_file = open(path, mode='w', newline='')
                    self.csv_writer = csv.writer(self.csv_file)
                    self.csv_writer.writerow(['Timestamp', 'Setup_V', 'Setup_A', 'Out_V', 'Out_A'])
                    self.logging_enabled = True
                    self.ui.logCSVButton.setText("STOP LOG")
                    print(f"Logging to {path}")
                except Exception as e:
                    print(f"Failed to open file: {e}")
        else:
            self.logging_enabled = False
            if self.csv_file:
                self.csv_file.close()
                self.csv_file = None
                self.csv_writer = None
                self.ui.logCSVButton.setText("LOG CSV")
                print("Logging stopped.")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
