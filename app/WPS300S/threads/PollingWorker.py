from PySide6.QtCore import QObject, Signal, QTimer, QElapsedTimer

class PollingWorker(QObject):
    data_ready = Signal(tuple)

    def __init__(self, device, interval=50):
        super().__init__()
        self.device = device
        self.interval = interval  # Polling interval (ms)
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.poll)
        self._last_emit_timer = QElapsedTimer()

    def start(self):
        self._last_emit_timer.start()
        self._timer.start(self.interval)

    def stop(self):
        self._timer.stop()

    def poll(self):
        setup = self.device.get_setup()
        vcm = self.device.get_actual_vcm()

        # Emit only every 100 ms
        if self._last_emit_timer.elapsed() >= 100:
            self.data_ready.emit((setup, vcm))
            self._last_emit_timer.restart()
