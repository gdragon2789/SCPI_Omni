import time
from decimal import Decimal
from api.__init__ import *
import re
class USER_SETUP(Enum):
    """
    user-saved settings that are stored in setup memory.
    """
    SETUP_0 = 0
    SETUP_1 = 1
    SETUP_2 = 2
    SETUP_3 = 3
    SETUP_4 = 4


class STATus(Enum):
    pass


class DeviceConst(Enum):
    SERIES = 'Series'
    PARALLEL = 'Parallel'
    NONE = 'NONE'
    ON = "1"
    OFF = "0"
    CH1 = "CH1"
    CH2 = "CH2"
    CH3 = "CH3"
    MAX_CURR =  6.0
    MIN_CURR = 0


class SYSTem(Enum):
    """
    This subsystem contains commands that affect the overall operation of the instrument, such as
    errors, versions, remote, local, beeper in the 9129B.
    """
    GET_SYSTem_ERRor = ":SYSTem:ERRor?"
    GET_SYSTem_VERSion = ":SYSTem:VERSion?"
    SET_SYSTem_REMote = ":SYSTem:REMote"
    SET_SYSTem_LOCal = ":SYSTem:LOCal"
    SET_SYSTem_BEEPer = ":SYSTem:BEEPer"


class OUTPut(Enum):
    """
    This command sets the state of channels CH1 + CH2 combined in series
    EXAMPLE:
        OUTP:STAT 0
        OUTP:SER 1
        OUTP:PAR 1
    """
    SET_OUTPut_ALL = ":OUTPut:STATe:ALL {state}"
    GET_OUTPut_ALL = ":OUTPut:STATe:ALL?"

    SET_OUTPut_SERies = ":OUTPut:SERies {state}"
    GET_OUTPut_SERies = ":OUTPut:SERies:STATe?"

    SET_OUTPut_PARallel = ":OUTPut:PARallel:STATe {state}"
    GET_OUTPut_PARallel = ":OUTPut:PARallel:STATe?"


class SOURce(Enum):
    SET_SOURce_CHANnel_OUTPut_STATe = ":SOURce:CHANnel:OUTPut:STATe {state}"
    GET_SOURce_CHANnel_OUTPut_STATe = ":SOURce:CHANnel:OUTPut:STATe?"

    SET_SOURce_OUTPut_PROTection_CLEar = ":SOURce:OUTPut:PROTection:CLEar"

    # Current
    SET_SOURce_CURRent_LEVel_IMMediate_AMPLitude = ":SOURce:CURRent:LEVel {value}"
    GET_SOURce_CURRent_LEVel_IMMediate_AMPLitude = ":SOURce:CURRent:LEVel:IMMediate:AMPLitude?"

    SET_SOURce_CURRent_LEVel_UP_IMMediate_AMPLitude = ":SOURce:CURRent:LEVel:UP:IMMediate:AMPLitude {value}"
    SET_SOURce_CURRent_LEVel_DOWN_IMMediate_AMPLitude = ":SOURce:CURRent:LEVel:DOWN:IMMediate:AMPLitude {value}"

    SET_SOURce_CURRent_LEVel_IMMediate_STEP_INCrement = ":SOURce:CURRent:LEVel:IMMediate:STEP:INCRement {value}"
    GET_SOURce_CURRent_LEVel_IMMediate_STEP_INCrement = ":SOURce:CURRent:LEVel:IMMediate:STEP:INCRement?"

    SET_SOURce_APPly_CURRent_LEVel_IMMediate_AMPLitude = ":SOURce:APPly:CURRent:LEVel:IMMediate:AMPLitude {value1}, {value2}, {value3}"
    GET_SOURce_APPly_CURRent_LEVel_IMMediate_AMPLitude = ":SOURce:APPly:CURRent:LEVel:IMMediate:AMPLitude?"

    SET_SOURce_APPly_OUTput_STATe = ":SOURce:APPly:OUTPut:STATe {state1}, {state2}, {state3}"
    GET_SOURce_APPly_OUTput_STATe = ":SOURce:APPly:OUTPut:STATe?"

    # Voltage
    SET_SOURce_APPly_VOLTage_LEVel_IMMediate_AMPLitude = ":SOURce:APPly:VOLTage:LEVel:IMMediate:AMPLitude {value1}, {value2}, {value3}"
    GET_SOURce_APPly_VOLTage_LEVel_IMMediate_AMPLitude = ":SOURce:APPly:VOLTage:LEVel:IMMediate:AMPLitude?"

    SET_SOURce_VOLTage_LEVel_UP_IMMediate_AMPLitude = ":SOURce:VOLTage:LEVel:UP:IMMediate:AMPLitude {value}"
    SET_SOURce_VOLTage_LEVel_DOWN_IMMediate_AMPLitude = ":SOURce:VOLTage:LEVel:DOWN:IMMediate:AMPLitude {value}"

    SET_SOURce_VOLTage_LEVel_IMMediate_STEP_INCrement = ":SOURce:VOLTage:LEVel:IMMediate:STEP:INCRement {value}"
    GET_SOURce_VOLTage_LEVel_IMMediate_STEP_INCrement = ":SOURce:VOLTage:LEVel:IMMediate:STEP:INCRement?"

    SET_SOURce_VOLTage_LIMIT_LEVel = ":SOURce:VOLTage:LIMIT:LEVel {value}"
    GET_SOURce_VOLTage_LIMIT_LEVel = ":SOURce:VOLTage:LIMIT:LEVel?"


class MEASure(Enum):
    GET_MEASure_SCALar_CURRent_DC = ":MEASure:SCALar:CURRent:DC {channel}?"
    GET_FETCh_CURRent_DC = ":FETCh:CURRent:DC?"

    GET_MEASure_SCALar_VOLTage_DC = ":MEASure:SCALar:VOLTage:DC {channel}?"
    GET_FETCh_VOLTage_DC = ":FETCh:VOLTage:DC?"

    GET_MEASure_SCALar_POWER_DC = ":MEASure:SCALar:POWER:DC {channel}?"
    GET_FETCh_POWER_DC = ":FETCh:POWER:DC?"

    GET_MEASure_SCALar_CURRent_ALL_DC = ":MEASure:SCALar:CURRent:ALL:DC?"
    GET_MEASure_SCALar_VOLTage_ALL_DC = ":MEASure:SCALar:VOLTage:ALL:DC?"


class INSTrument(Enum):
    SET_INSTrument_SELect = ':INSTrument:SELect {channel}'
    GET_INSTrument_SELect = ":INSTrument:SELect?"

    SET_INSTrument_NSELect = ":INSTrument:NSELect {channel}"
    GET_INSTrument_NSELect = ":INSTrument:NSELect?"

    SET_INSTrument_COMbine_SERies = ":INSTrument:COMbine:SERies"
    SET_INSTrument_COMbine_PARAllel = ":INSTrument:COMbine:PARAllel"
    SET_INSTrument_COMbine_OFF = ":INSTrument:COMbine:OFF"

    GET_INSTrument_COMbine = ":INSTrument:COMbine?"


class BK9129B(VISA_INSTRUMENT):
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

    def coupling_series(self):
        cmd = INSTrument.SET_INSTrument_COMbine_SERies.value
        self.write(command=cmd)

        #check the status
        self.device_validator(command=INSTrument.GET_INSTrument_COMbine.value,
                              result=DeviceConst.SERIES.value)

    def select_channel(self, channel):
        cmd = INSTrument.SET_INSTrument_SELect.value.format(channel=channel)
        self.write(cmd)

        # Todo: Check the current channel
        # check the status


    def coupling_parallel(self):
        cmd = INSTrument.SET_INSTrument_COMbine_PARAllel.value
        self.write(command=cmd)

        #check the status
        self.device_validator(command=INSTrument.GET_INSTrument_COMbine.value,
                              result=DeviceConst.PARALLEL.value)

    def coupling_off(self):
        cmd = INSTrument.SET_INSTrument_COMbine_OFF.value
        self.write(cmd)

        #check the status
        self.device_validator(command=INSTrument.GET_INSTrument_COMbine.value,
                              result=DeviceConst.NONE.value)

    def enable_all_output(self):
        cmd = OUTPut.SET_OUTPut_ALL.value.format(state=DeviceConst.ON.value)
        self.write(cmd)
        #check the status
        self.device_validator(command=OUTPut.GET_OUTPut_ALL.value,
                              result=DeviceConst.ON.value)

    def disable_all_output(self):
        cmd = OUTPut.SET_OUTPut_ALL.value.format(state=DeviceConst.OFF.value)
        self.write(cmd)
        #check the status
        self.device_validator(command=OUTPut.GET_OUTPut_ALL.value,
                              result=DeviceConst.OFF.value)

    def enable_series_output(self):
        cmd = OUTPut.SET_OUTPut_SERies.value.format(state=DeviceConst.ON.value)
        self.write(cmd)
        #check the status
        self.device_validator(command=OUTPut.GET_OUTPut_SERies.value,
                              result=DeviceConst.ON.value)

    def disable_series_output(self):
        cmd = OUTPut.SET_OUTPut_SERies.value.format(state=DeviceConst.OFF.value)
        self.write(cmd)
        #check the status
        self.device_validator(command=OUTPut.GET_OUTPut_SERies.value,
                              result=DeviceConst.OFF.value)

    def enable_parallel_output(self):
        cmd = OUTPut.SET_OUTPut_PARallel.value.format(state=DeviceConst.ON.value)
        self.write(cmd)
        # check the status
        self.device_validator(command=OUTPut.GET_OUTPut_PARallel.value,
                              result=DeviceConst.ON.value)

    def disable_parallel_output(self):
        cmd = OUTPut.SET_OUTPut_PARallel.value.format(state=DeviceConst.OFF.value)
        self.write(cmd)
        # check the status
        self.device_validator(command=OUTPut.GET_OUTPut_PARallel.value,
                              result=DeviceConst.OFF.value)

    def enable_output(self, channel):
        self.select_channel(channel=channel)

        cmd = SOURce.SET_SOURce_CHANnel_OUTPut_STATe.value.format(state=DeviceConst.ON.value)
        self.write(cmd)
        # # check the status
        # self.device_validator(command=SOURce.GET_SOURce_CHANnel_OUTPut_STATe.value,
        #                       result=DeviceConst.ON.value)

    def disable_output(self, channel):
        self.select_channel(channel=channel)

        cmd = SOURce.SET_SOURce_CHANnel_OUTPut_STATe.value.format(state=DeviceConst.OFF.value)
        self.write(cmd)
        # check the status
        # self.device_validator(command=SOURce.GET_SOURce_CHANnel_OUTPut_STATe.value,
        #                       result=DeviceConst.OFF.value)

    def clear_power_supply_protect(self):
        """
        This instruction is used to clear protected power supply,
        such as the protection OVP and OTP protection
        :return:
        """
        cmd = SOURce.SET_SOURce_OUTPut_PROTection_CLEar.value
        self.write(cmd)
        return True

    def set_current(self, channel = "CH1" ,curr=0.0) -> None:
        """
        This command is used to set the current value of the selected channel.
        :param channel:
        :param curr:
        :return:
        """
        self.select_channel(channel=channel)

        if float(curr) < float(DeviceConst.MIN_CURR.value) or float(curr) > float(DeviceConst.MAX_CURR.value):
            cmd = SOURce.SET_SOURce_CURRent_LEVel_IMMediate_AMPLitude.value.format(value=1.0)
            self.write(cmd)
            raise ValueError("Out of working range (0-3.1A) - Restore to default")
        else:
            cmd = SOURce.SET_SOURce_CURRent_LEVel_IMMediate_AMPLitude.value.format(value=curr)
            self.write(cmd)

            # self.device_validator(command=SOURce.GET_SOURce_CURRent_LEVel_IMMediate_AMPLitude.value,
            #                       result=self.strip_trailing_zeros(n=curr))

    def set_voltage(self, channel = "CH1", volt=0.0) -> None:
        """

        :param channel:
        :param volt:
        :return:
        """
        self.select_channel(channel=channel)

        cmd = SOURce.GET_SOURce_APPly_VOLTage_LEVel_IMMediate_AMPLitude.value
        current_voltage_level = self.query(cmd)
        current_voltage_level = current_voltage_level.split(", ")
        volt1 = current_voltage_level[0]
        volt2 = current_voltage_level[1]
        volt3 = current_voltage_level[2]
        volt_target = volt
        if channel == DeviceConst.CH1.value:
            volt1 = volt_target
            volt2 = volt2
            volt3 = volt2
        elif channel == DeviceConst.CH2.value:
            volt1 = volt1
            volt2 = volt_target
            volt3 = volt3
        elif channel == DeviceConst.CH3.value:
            volt1 = volt1
            volt2 = volt2
            volt3 = volt_target
        cmd = SOURce.SET_SOURce_APPly_VOLTage_LEVel_IMMediate_AMPLitude.value.format(value1=volt1,
                                                                                     value2=volt2,
                                                                                     value3=volt3)
        self.write(cmd)

        # Todo check the status return and validate
        # self.device_validator(command=SOURce.GET_SOURce_APPly_VOLTage_LEVel_IMMediate_AMPLitude.value,
        #                       result=self.strip_trailing_zeros(n=volt))

    def get_voltage(self):
        result = {
            "CH1": 0.0,
            "CH2": 0.0,
            "CH3": 0.0
        }
        cmd = MEASure.GET_MEASure_SCALar_VOLTage_ALL_DC.value
        current_voltage_level = self.query(cmd)
        current_voltage_level = current_voltage_level.split(", ")
        result["CH1"] = current_voltage_level[0]
        result["CH2"] = current_voltage_level[1]
        result["CH3"] = current_voltage_level[2]

        return result

    def get_current(self):
        result = {
            "CH1": 0.0,
            "CH2": 0.0,
            "CH3": 0.0
        }
        cmd = MEASure.GET_MEASure_SCALar_CURRent_ALL_DC.value
        current_current_level = self.query(cmd)
        current_current_level = current_current_level.split(", ")
        result["CH1"] = current_current_level[0]
        result["CH2"] = current_current_level[1]
        result["CH3"] = current_current_level[2]

        return result

if __name__ == '__main__':
    scanner = PyVISAScanner()
    scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="9129B")

    instr = BK9129B(visa_port=port, connection_type=connect_type)

    instr.enable_remote()
    # instr.disable_remote()
    instr.enable_remote()
    # instr.coupling_series()
    # instr.coupling_parallel()
    # instr.coupling_off()
    # instr.enable_all_output()
    # instr.disable_all_output()
    # instr.enable_output(channel="CH1")
    # instr.disable_output(channel="CH1")
    # for i in range(3):
    #     instr.set_current(curr=i)
    #     time.sleep(1)
    # instr.set_voltage(channel="CH1",volt=3)
    # instr.set_voltage(channel="CH2",volt=3)
    # instr.set_voltage(channel="CH3",volt=3)
    # for i in range(1,6):
    #     for j in range(1,4):
    #         instr.set_voltage(channel=f"CH{j}", volt=i)

    # instr.set_voltage(channel="CH1", volt=60)
    # print("End debug")

    print(instr.get_voltage())
    print(instr.get_current())
    # instr.controller.close()
