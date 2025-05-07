import json
from instrument.Digital_Multimeter.DMM6500 import *


def my_function():
    scanner = PyVISAScanner()
    connect_type, port = scanner.scan_for_instruments(expected_id="DMM6500")
    instr = DMM6500_V1(visa_port=port, connection_type=connect_type)
    print("Current Test")
    instr.set_range(function=FUNCTION.CURR_DC.value,
                        n=RANGE.AC_100mA.value)
    value = round(float(instr.measure_with(function=FUNCTION.CURR_DC.value)),ndigits=3)
    print(f"{value} mA")
    instr.close()
    return {"function": FUNCTION.CURR_DC.value, "value": value}

if __name__ == '__main__':
    # Run the function and print its output in JSON format
    output = my_function()
    # print(json.dumps(output))
    print(output)
