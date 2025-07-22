from api.__init__ import *
from decimal import Decimal
import re

class DeviceConst(Enum):
    pass

class INSTRUMENT_NAME(VISA_INSTRUMENT):
    def __init__(self, visa_port=None, connection_type=None):
        super().__init__(visa_port, connection_type)
        self.soft_delay = 0.3

    def device_validator(self,command, result):
        res = self.query(command=command)
        a = self.strip_trailing_zeros(result)
        if res == str(a):
            print("Success")
            return True
        else:
            print(res)
            print(type(res))
            raise ValueError(f"Can not set the device to {result} MODE")

    @staticmethod
    def strip_trailing_zeros(n):
        pattern = r'^-?\d+(\.\d+)?$'
        n = str(n)
        if bool(re.match(pattern, n)):
            n = float(n)
            d = Decimal(str(n)).normalize()
            if d == d.to_integral():
                return int(d)
            return float(d)
        else:
            return n

if __name__ == '__main__':
    scanner = PyVISAScanner()
    scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="INSTRUMENT_NAME")

    instr = INSTRUMENT_NAME(visa_port=port, connection_type=connect_type)
    instr.controller.close()