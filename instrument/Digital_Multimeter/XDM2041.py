from api.__init__ import *
from decimal import Decimal
import re

class DeviceConst(Enum):
    pass

class SENSe(Enum):
    SET_SENSe_FUNCtion = 'SENSe:FUNCtion "{function}"'
    GET_SENSe_FUNCtion = 'SENSe:FUNCtion[1]?'

class CONFigure(Enum):
    pass

class CALCulate(Enum):
    pass

class SYSTem(Enum):
    SET_REMOTE = 'SYSTem:REMote'
    SET_LOCAL  = 'SYSTem:LOCAl'
class OTHer(Enum):
    pass

class XDM2041(VISA_INSTRUMENT):
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

    def enable_remote(self):
        cmd = SYSTem.SET_REMOTE.value
        self.write(command=cmd)

    def enable_local(self):
        cmd = SYSTem.SET_LOCAL.value
        self.write(command=cmd)

    

if __name__ == '__main__':
    scanner = PyVISAScanner()
    # scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="XDM2041")
    instr = XDM2041(visa_port=port, connection_type=connect_type)

    # instr.set_mode(function="RES")

    instr.enable_remote()

    a = instr.get_mode()
    print(instr.get_mode())


    instr.controller.close()