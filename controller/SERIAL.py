# scpi_uart.py
import serial
import time

class SERIAL_Controller:
    # Try common / modern baudrates first
    BAUDRATES = (115200, 9600, 57600, 38400, 19200,  4800, 2400)
    IDN_MAX_ATTEMPTS = 3
    IDN_RETRY_DELAY = 0.2  # seconds
    PORT_SETTLE_DELAY = 0.3  # after opening the port

    def __init__(self,
                 port: str,
                 buffer_size: int = 4096,
                 timeout: float = 1.0,
                 debug: bool = False) -> None:
        """
        Initializes the SERIAL_Controller class for communicating with SCPI instruments over UART.

        :param port: The serial port (e.g., 'COM3' or '/dev/ttyUSB0').
        :param buffer_size: Size of the buffer for reading responses.
        :param timeout: Read timeout in seconds used during port scan.
        :param debug: Enable debug prints if True.
        """
        self.buffer_size = buffer_size
        self.debug = debug
        self._timeout = timeout

        self._connection = None
        self._idn = None

        # Scan the port at known baudrates
        self.port_scan(port)

    def port_scan(self, port: str) -> bool:
        for baudrate in self.BAUDRATES:
            try:
                print(f"Trying {port} at {baudrate} baud...")

                self._connection = serial.Serial(
                    port=port,
                    baudrate=baudrate,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=self._timeout,
                )

                # Allow device/USB bridge to settle
                time.sleep(self.PORT_SETTLE_DELAY)

                # Clear any garbage
                self._connection.reset_input_buffer()
                self._connection.reset_output_buffer()

                idn = self._try_idn_query()

                if idn:
                    self._idn = idn
                    print(f"Connected to {idn.strip()} at {baudrate} baud.")
                    return True

                if self.debug:
                    print(f"No *IDN? response at {baudrate} baud, closing port.")
                self.close()

            except Exception as e:
                if self.debug:
                    print(f"Error on {port} at {baudrate} baud: {e}")
                self.close()
                continue

        print(f"UART instrument could not be identified on {port} at any known baudrate.")
        return False

    def _try_idn_query(self) -> str:
        """
        Try *IDN? a few times with short delays.
        Returns the first non-empty response, or "" if none.
        """
        for attempt in range(1, self.IDN_MAX_ATTEMPTS + 1):
            idn = self.query("*IDN?\n")
            if idn and idn.strip():
                if self.debug:
                    print(f"*IDN? succeeded on attempt {attempt}")
                return idn

            if self.debug:
                print(f"*IDN? attempt {attempt} failed, retrying in {self.IDN_RETRY_DELAY}s...")
            time.sleep(self.IDN_RETRY_DELAY)

        return ""

    def write(self, command: str) -> None:
        """
        Sends a SCPI command to the instrument.

        :param command: SCPI command string.
        """
        command += "\n"  # Add termination
        self._connection.write(command.encode())

    def query(self, command: str) -> str:
        self._connection.reset_input_buffer()
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

    def close(self,soft_delay=0.5) -> None:
        """Closes the UART connection."""

        self._connection.close()
        time.sleep(soft_delay)

    @property
    def idn(self):
        return self._idn