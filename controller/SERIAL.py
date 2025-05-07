# scpi_uart.py
import serial
import time

class SERIAL_Controller:
    def __init__(self,
                 port: str,
                 baudrate: int = 9600,
                 timeout: float | None = 0.01,
                 buffer_size: int = 4096,
                 debug=False) -> None:
        """
        Initializes the UART_Controller class for communicating with SCPI instruments over UART.

        :param port: The serial port (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Baud rate for the UART connection.
        :param timeout: Read timeout in seconds.
        :param buffer_size: Size of the buffer for reading responses.
        """
        self._connection = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=timeout
        )
        self.buffer_size = buffer_size
        self.debug = debug
        self._idn = None  # <-- Initialize first!

        idn = self.query("*IDN?")
        if idn:
            self._idn = idn
            if self.debug:
                print(f"Connected to {idn}.")
            self.write(command="*RST")
        else:
            self.close()
            if self.debug:
                print("UART Instrument could not be identified.")


    def write(self, command: str) -> None:
        """
        Sends a SCPI command to the instrument.

        :param command: SCPI command string.
        """
        command += "\n"  # Add termination
        self._connection.write(command.encode())

    def query(self, command: str) -> str:
        self.write(command)
        recv_bytes = b""
        start_time = time.time()
        timeout_duration = 2  # seconds

        while True:
            recv_bytes += self._connection.read(self.buffer_size)
            if recv_bytes.endswith(b"\n"):
                return recv_bytes.decode(errors="ignore").strip()
            if time.time() - start_time > timeout_duration:
                # Timeout, no good reply
                break
        return ""

    def close(self) -> None:
        """Closes the UART connection."""
        self._connection.close()

    @property
    def idn(self):
        return self._idn