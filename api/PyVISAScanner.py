import pyvisa
import platform
import re
import os
import sys

# Lấy thư mục hiện tại của file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lên 2 cấp để đến thư mục SCPI_Omni
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Thêm vào sys.path nếu chưa có
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from controller.SERIAL import SERIAL_Controller
from controller.TCPIP import TCPIP_Controller



class PyVISAScanner:
    def __init__(self):
        if platform.system() == "Windows":
            self.__resource_manager = pyvisa.ResourceManager()
        else:
            self.__resource_manager = pyvisa.ResourceManager("@py")
        self.__resource_store = self.__resource_manager.list_resources()
        self.__hardware_store = []
        self.__scanner_initial()
        # print("Here: ",self.__hardware_store)

    def __scanner_initial(self):
        for resource in self.__resource_store:
            result = self.__decompose_resource_visa(resource)
            if result["resource_type"] == "INSTR":
                self.__hardware_store.append(result)
            else:
                pass

    @staticmethod
    def __decompose_resource_visa(resource_string: str)-> dict:
        # USB Connection (USB - Universal Serial Bus)
        usb_result_dict = {
            "connect_type": str,
            "vid": str,
            "pid": str,
            "sn": str,
            "resource_type": str,
            "visa_id":str,
        }
        # TCP/IP Connection (TCPIP - Transport Control Protocol/Internet Protocol)
        tcp_result_dict = {
            "connect_type": str,
            "ip": str,
            "port": str,
            "resource_type": str,
            "visa_id": str,
        }
        # Serial Connection (ASLR - Asynchronous Serial Resource Locator)
        serial_result_dict = {
            "connect_type": str,
            "port": str,
            "resource_type": str,
            "visa_id": str,
        }

        components = resource_string.split("::")

        if components[0].startswith("USB"):
            usb_result_dict["connect_type"] = "USB"
            usb_result_dict["vid"] = components[1]
            usb_result_dict["pid"] = components[2]
            usb_result_dict["sn"] = components[3]
            usb_result_dict["resource_type"] = components[4]
            usb_result_dict["visa_id"] = resource_string
            return usb_result_dict

        elif components[0].startswith("TCPIP"):
             tcp_result_dict["connect_type"] = "TCP/IP"
             tcp_result_dict["ip"] = components[1]
             tcp_result_dict["port"] = components[2]
             tcp_result_dict["resource_type"] = components[3]
             tcp_result_dict["visa_id"] = resource_string
             return tcp_result_dict

        elif components[0].startswith("ASRL"):
            serial_result_dict["connect_type"] = "Serial"
            os_name = platform.system()
            raw_port = components[0][4:]

            if os_name == "Windows":
                # On Windows, it will just be a number, e.g., ASRL3 => COM3
                serial_result_dict["port"] = f"COM{raw_port}"

            else:
                # On Linux/Mac, it will already be something like /dev/ttyUSB0
                serial_result_dict["port"] = raw_port
            serial_result_dict["resource_type"] = components[1]
            serial_result_dict["visa_id"] = resource_string
            return serial_result_dict

        else:
            return {
                "connect_type": "Unknown",}

    @staticmethod
    def __decompose_instrument_name(resource_string: str)-> dict:
        # USB Connection (USB - Universal Serial Bus)
        dict_name = {
            "manufacturer": "Unknown",
            "model": "Unknown",
            "sn": "Unknown",
            "firmware_version": "Unknown",
        }
        print(resource_string)
        if resource_string is not None:
            components = resource_string.split(",")
            if len(components) == 4:
                dict_name["manufacturer"] = components[0]
                dict_name["model"] = components[1]
                dict_name["sn"] = components[2]
                dict_name["firmware_version"] = components[3]
                return dict_name
            elif len(components) == 3:
                dict_name["manufacturer"] = components[0]
                dict_name["model"] = components[1]
                dict_name["firmware_version"] = components[2]
                return dict_name
        return dict_name

    def scan_instruments_v0(self):
        """
        Scans all connected instruments and checks their *IDN? response.

        :return: The resource string of the matching instrument, or None if not found.
        """
        available_instruments = {
            "instr": str,
            "connection_type": str,
            "connection": str
        }

        for device in self.__hardware_store:
            try:
                if device["connect_type"] == "USB":
                    with self.__resource_manager.open_resource(device["visa_id"]) as instrument:
                        instrument.timeout = 0.001  # Set a timeout for the query
                        response = instrument.query('*IDN?').strip()
                        split_response = self.__decompose_instrument_name(response)
                        available_instruments["instr"] = split_response["model"]
                        available_instruments["connection_type"] = device["connect_type"]
                        available_instruments["connection"] = device["visa_id"]
                        print(available_instruments)
                elif device["connect_type"] == "TCP/IP":
                    instrument = TCPIP_Controller(ip_address=device["ip"])
                    split_response = self.__decompose_instrument_name(instrument.idn)
                    instrument.close()
                    available_instruments["instr"] = split_response["model"]
                    available_instruments["connection_type"] = device["connect_type"]
                    available_instruments["connection"] = device["ip"]
                    print(available_instruments)
                elif device["connect_type"] == "Serial":
                    instrument = SERIAL_Controller(port=device["port"])
                    split_response = self.__decompose_instrument_name(instrument.idn)
                    instrument.close()
                    available_instruments["instr"] = split_response["model"]
                    available_instruments["connection_type"] = device["connect_type"]
                    available_instruments["connection"] = device["port"]
                    print(available_instruments)
            except pyvisa.VisaIOError as e:
                print(f"Error on {device}: {e}")
        return None

    def scan_instruments(self):
        """
        Scans all connected instruments and checks their *IDN? response.

        :return: The resource string of the matching instrument, or None if not found.
        """
        for device in self.__hardware_store:
            try:
                if device["connect_type"] == "USB":
                    with self.__resource_manager.open_resource(device["visa_id"]) as instrument:
                        response = instrument.query('*IDN?').strip()
                        model = self.__decompose_instrument_name(response)["model"]
                elif device["connect_type"] == "TCP/IP":
                    instrument = TCPIP_Controller(ip_address=device["ip"])
                    model = self.__decompose_instrument_name(instrument.idn)["model"]
                    instrument.close()
                elif device["connect_type"] == "Serial":
                    instrument = SERIAL_Controller(port=device["port"])
                    model = self.__decompose_instrument_name(instrument.idn)["model"]
                    instrument.close()
                else:
                    continue

                available_instruments = {
                    "instr": model,
                    "connection_type": device["connect_type"],
                    "connection": device["visa_id"] if "visa_id" in device else device["ip"] if "ip" in device else
                    device["port"]
                }
                # print(available_instruments)

            except pyvisa.VisaIOError as e:
                print(f"Error on {device}: {e}")

        return None

    def scan_for_instruments(self, expected_id: str):
        """
        Scans specify instruments and checks their *IDN? response.

        :param expected_id: The expected identifier string from the *IDN? response.
        :return: The resource string of the matching instrument, or None if not found.
        """

        """
        Scans all connected instruments and checks their *IDN? response.

        :return: The resource string of the matching instrument, or None if not found.
        """
        available_instruments = {
            "instr": str,
            "connection_type": str,
            "connection": str
        }

        for device in self.__hardware_store:
            split_response = None
            try:
                if device["connect_type"] == "USB":
                    with self.__resource_manager.open_resource(device["visa_id"]) as instrument:
                        instrument.timeout = 2000  # Set a timeout for the query
                        response = instrument.query('*IDN?').strip()
                        split_response = self.__decompose_instrument_name(response)
                        available_instruments["instr"] = split_response["model"]
                        available_instruments["connection_type"] = device["connect_type"]
                        available_instruments["connection"] = device["visa_id"]
                elif device["connect_type"] == "TCP/IP":
                    instrument = TCPIP_Controller(ip_address=device["ip"])
                    split_response = self.__decompose_instrument_name(instrument.idn)
                    available_instruments["instr"] = split_response["model"]
                    available_instruments["connection_type"] = device["connect_type"]
                    available_instruments["connection"] = device["ip"]
                    instrument.close()
                elif device["connect_type"] == "Serial":
                    instrument = SERIAL_Controller(port=device["port"])
                    split_response = self.__decompose_instrument_name(instrument.idn)
                    available_instruments["instr"] = split_response["model"]
                    available_instruments["connection_type"] = device["connect_type"]
                    available_instruments["connection"] = device["port"]
                    instrument.close()

                for item in split_response.values():
                    if re.search(expected_id, item):
                        print(f"Instrument found: {available_instruments['instr']} on {available_instruments['connection']}")
                        return available_instruments["connection_type"],available_instruments["connection"],

            except pyvisa.VisaIOError as e:
                print(f"Error on {device}: {e}")
        return None

    def list_device(self):
        for device in self.__hardware_store:
            print(device)
        return None


if __name__ == "__main__":
    scanner = PyVISAScanner()
    scanner.list_device()
    scanner.scan_instruments()
    # scanner.scan_for_instruments(expected_id="WPS300S-15005")
    # For WPS300S-15005 there are a bug on connect and disconnect,
    # it requires a delay long time to response,
    # so I increase the time after close the connection to 0.5s
    # scanner.scan_for_instruments(expected_id="SDM3055")
    # scanner.scan_for_instruments(expected_id="DMM6500")
    # scanner.scan_for_instruments(expected_id="SPE6053")

    # scanner.scan_for_instruments(expected_id="SDL1020X")

