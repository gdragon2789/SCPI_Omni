import time

from api.__init__ import *
from decimal import Decimal
import re

class DeviceConst(Enum):
    ON = "1"
    OFF = "0"

class SYSTem(Enum):
    SET_SYSTem_REMote = ":SYSTem:REMote"
    SET_SYSTem_LOCal = ":SYSTem:LOCal"
    SET_SYSTem_BEEP = ":SYSTem:BEEP {state}"
    GET_SYSTem_BEEP = ":SYSTem:BEEP?"
    GET_SYSTem_ERRor = ":SYSTem:ERRor?"
    GET_SYSTem_TEMP = ":SYSTem:TEMP?"

class APPLy(Enum):
    SET_APPLy = ":APPLy{voltage},{current}"
    GET_APPLy = ":APPLy?"

class MEASure(Enum):
    GET_MEASure_VOLTage = ":MEASure:VOLTage?"
    GET_MEASure_CURRent = ":MEASure:CURRent?"
    GET_MEASure_POWER = ":MEASure:POWER?"
    GET_MEASure_VCM = ":MEASure:VCM?"

class OUTPut(Enum):
    SET_OUTPut = ":OUTPut {state}"
    GET_OUTPut = ":OUTPut?"

class VOLTage(Enum):
    SET_VOLTage = ":VOLTage {voltage}"
    GET_VOLTage = ":VOLTage?"
    SET_VOLTage_MIN = ":VOLTage:MIN {voltage}"
    GET_VOLTage_MIN = ":VOLTage:MIN?"
    SET_VOLTage_MAX = ":VOLTage:MAX {voltage}"
    GET_VOLTage_MAX = ":VOLTage:MAX?"
    SET_VOLTage_PROTection = ":VOLTage:PROTection {volt}"
    GET_VOLTage_PROTection = ":VOLTage:PROTection?"
    SET_VOLTage_PROTection_STATE = ":VOLTage:PROTection:STATe {state}"
    GET_VOLTage_PROTection_STATE = ":VOLTage:PROTection:STATe?"

class CURRent(Enum):
    SET_CURRent = ":CURRent {current}"
    GET_CURRent = ":CURRent?"
    SET_CURRent_MIN = ":CURRent:MIN {current}"
    GET_CURRent_MIN = ":CURRent:MIN?"
    SET_CURRent_MAX = ":CURRent:MAX {current}"
    GET_CURRent_MAX = ":CURRent:MAX?"
    SET_CURRent_PROTection = ":CURRent:PROTection {curr}"
    GET_CURRent_PROTection = ":CURRent:PROTection?"
    SET_CURRent_PROTection_STATE = ":CURRent:PROTection:STATe {state}"
    GET_CURRent_PROTection_STATE = ":CURRent:PROTection:STATe?"

class WPS300S(VISA_INSTRUMENT):
    def __init__(self, visa_port=None, connection_type=None):
        super().__init__(visa_port, connection_type)

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
        cmd = SYSTem.SET_SYSTem_REMote.value
        self.write(command=cmd)

    def disable_remote(self):
        cmd = SYSTem.SET_SYSTem_LOCal.value
        self.write(command=cmd)

    def enable_beeper(self):
        cmd = SYSTem.SET_SYSTem_BEEP.value.format(state=DeviceConst.ON.value)
        self.write(command=cmd)

        #check the status
        self.device_validator(command=SYSTem.GET_SYSTem_BEEP.value,
                              result=DeviceConst.ON.value)

    def disable_beeper(self):
        cmd = SYSTem.SET_SYSTem_BEEP.value.format(state=DeviceConst.OFF.value)
        self.write(command=cmd)

        #check the status
        self.device_validator(command=SYSTem.GET_SYSTem_BEEP.value,
                              result=DeviceConst.OFF.value)
if __name__ == '__main__':
    scanner = PyVISAScanner()
    # scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="WPS300S-15005")

    instr = WPS300S(visa_port=port, connection_type=connect_type)
    instr.enable_remote()
    instr.enable_beeper()
    
    instr.disable_beeper()
    instr.controller.close()