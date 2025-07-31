import time
import os
import sys
# Lấy thư mục hiện tại của file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lên 2 cấp để đến thư mục SCPI_Omni
<<<<<<< HEAD
parent_dir = os.path.abspath(os.path.join(current_dir,".." ,".."))
=======
parent_dir = os.path.abspath(os.path.join(current_dir,".." ,".." ,".."))
>>>>>>> c07369b2556f66b8e2d21fcf24a4423b153bd87c

# Thêm vào sys.path nếu chưa có
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from api.__init__ import *
from decimal import Decimal
import re

DEBUG_MESSAGE = "Ohayogozaimasu, WPS300S-15005"

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
    SET_APPLy = ":APPLy {voltage},{current}"
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
    SET_VOLTage_PROTection = ":VOLTage:PROTection {voltage}"
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
    SET_CURRent_PROTection = ":CURRent:PROTection {current}"
    GET_CURRent_PROTection = ":CURRent:PROTection?"
    SET_CURRent_PROTection_STATE = ":CURRent:PROTection:STATe {state}"
    GET_CURRent_PROTection_STATE = ":CURRent:PROTection:STATe?"

class WPS300S(VISA_INSTRUMENT):
    def __init__(self, visa_port=None, connection_type=None):
        super().__init__(visa_port, connection_type)
        self.enable_remote()
        self.slew_rate = 0.15 # Need to measure
        self.now_voltage = 0
        self.now_current = 0
        self.get_setup()
        print(self.now_voltage, self.now_current)

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

    # Basic commands
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

    def get_setup(self):
        cmd = APPLy.GET_APPLy.value
        results =self.query(command=cmd).split(sep=",")
        float_list = [float(x) for x in results]
        self.now_voltage = float_list[0]
        self.now_current = float_list[1]
        return float_list
    

    def setup(self,volt=0.0, curr=0.0):
        cmd = APPLy.SET_APPLy.value.format(voltage=volt, current=curr)
        self.write(command=cmd)
            
        #check the status
        results = self.get_setup()
        if results[0] == volt and results[1] == curr:
            print("Success")
            return True
        else:
            print("Failed")
            return False

    def get_actual_voltage(self):
        cmd = MEASure.GET_MEASure_VOLTage.value
        result = self.query(command=cmd)
        print(f"Actual Voltage: {result}")
        return float(result)

    def get_actual_current(self):
        cmd = MEASure.GET_MEASure_CURRent.value
        result = self.query(command=cmd)
        print(f"Actual Current: {result}")
        return float(result)

    def get_actual_power(self):
        cmd = MEASure.GET_MEASure_POWER.value
        result = self.query(command=cmd)
        print(f"Actual Power: {result}")
        return float(result)

    def get_actual_vcm(self):
        cmd = MEASure.GET_MEASure_VCM.value
        results =self.query(command=cmd).split(sep=",")
        float_list = [float(x) for x in results]
        print(f"Actual VCM: {float_list}")
        return float_list
    
    def enable_output(self):
        cmd = OUTPut.SET_OUTPut.value.format(state=1)
        self.write(command=cmd)
        time.sleep(self.now_voltage * self.slew_rate)
         
    
    def disable_output(self):
        cmd = OUTPut.SET_OUTPut.value.format(state=0)
        self.write(command=cmd)
        time.sleep(self.now_voltage * self.slew_rate)

    # Protection command
    def set_ovp(self, voltage):
        cmd = VOLTage.SET_VOLTage_PROTection.value.format(voltage=voltage)
        self.write(command=cmd)

        state = self.query(command=VOLTage.GET_VOLTage_PROTection_STATE.value)
        print(state)

    def set_ocp(self, current):
        cmd = CURRent.SET_CURRent_PROTection.value.format(current=current)
        self.write(command=cmd)

        state = self.query(command=CURRent.GET_CURRent_PROTection_STATE.value)
        print(state)


    def setup_protection(self, ovp=0.0, ocp=0.0):
        self.set_ovp(voltage=ovp)
        self.set_ocp(current=ocp)

    def min_setup(self, min_volt=0.0, min_curr=0.0):
        cmd = VOLTage.SET_VOLTage_MIN.value.format(voltage=min_volt)
        self.write(command=cmd)
        cmd = CURRent.SET_CURRent_MIN.value.format(current=min_curr)
        self.write(command=cmd)

    def max_setup(self, max_volt=0.0, max_curr=0.0):
        cmd = VOLTage.SET_VOLTage_MAX.value.format(voltage=max_volt)
        self.write(command=cmd)
        cmd = CURRent.SET_CURRent_MAX.value.format(current=max_curr)
        self.write(command=cmd)

    def min_max_setup(self, min_volt=0.0, min_curr=0.0, max_volt=0.0, max_curr=0.0):
        self.min_setup(min_volt=min_volt, min_curr=min_curr)
        self.max_setup(max_volt=max_volt, max_curr=max_curr)



if __name__ == '__main__':
    scanner = PyVISAScanner()
    # scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="WPS300S-15005")

    instr = WPS300S(visa_port=port, connection_type=connect_type)
    instr.enable_remote()
    instr.enable_beeper()
    instr.setup(volt=12.0, curr=1.0)
<<<<<<< HEAD
    instr.setup(volt=24.0, curr=1.0)
    instr.setup(volt=48.0, curr=1.0)
=======
    time.sleep(2)
    instr.setup(volt=24.0, curr=1.0)
    time.sleep(2)
    instr.setup(volt=48.0, curr=1.0)
    time.sleep(2)
>>>>>>> c07369b2556f66b8e2d21fcf24a4423b153bd87c
    instr.enable_output()
    instr.get_actual_voltage()
    instr.get_actual_current()
    instr.get_actual_power()
    instr.get_actual_vcm()
    instr.disable_output()
    instr.get_actual_voltage()
    instr.get_actual_current()
    instr.get_actual_power()
    instr.get_actual_vcm()
    
    # instr.disable_beeper()
    # instr.controller.close()