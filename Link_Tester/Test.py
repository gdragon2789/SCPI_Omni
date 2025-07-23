from Ulity.DynamicUIPlace import DynamicUI
import tkinter as tk
import time
import json
import re

Application = DynamicUI("Config/gui_config.csv")
CONFIG = json.load(open("Config/config.json"))

class testBase:
    def __init__(self):
        self.name = None
        self.description = None
        self.result = None
        self.error = None

        self.t_start = None
        self.t_end = None
        self.duration = None

    def run(self):
        pass

    def cleanup(self):
        pass

class scanID(testBase):
    def __init__(self, app):
        super().__init__()
        self.name = "Scan_ID"
        self.description = "Scan for board ID"
        self.app = app
        self.widget = app.widget
        self.boardID = "Empty"
        self.t_start = 0
        self.t_end = 0
        self.duration = 0

    def run(self):
        self.t_start = time.time()
        if self._check_loop():
            self.result = "Pass"
            return True
        # self.cleanup()

    def _check_loop(self):
        self.widget.entrySerial.focus_set()
        self.boardID = self.widget.entrySerial.get()
        if len(self.boardID) == CONFIG["serial_pattern"]["length"] and re.match(CONFIG["serial_pattern"]["pattern"], self.boardID):
            self.widget.entrySerial.disable()
            print(f"Match found: {self.boardID}")

            self.t_end = time.time()
            self.duration = self.t_end - self.t_start
            print(f"Duration: {self.duration}")
            return True
        else:
            print(f"No match found: {self.boardID}")
            self.widget.entrySerial.clear()
            self.app.root.after(1000, self._check_loop)  # Re-run after 100 ms (0.1 sec)

    def cleanup(self):
        self.widget.entrySerial.enable()
        self.widget.entrySerial.clear()
        self.t_start = 0
        self.t_end = 0
        self.duration = 0

class TestCases:
    def __init__(self, app):
        self.app = app
        self.mode_var = self.app.widget.testMode
        self.ready_var = self.app.widget.selectButton


        self.testcases = [
            scanID(app=self.app),
        ]

    def select_mode(self):
        if self.app.widget.selectButton.pressed():
            print(f"Selected Mode {self.app.widget.testMode.get()}")
        else:
            print("Not selected")
            self.app.root.after(1000, self.select_mode)


    def run(self):
        for testcase in self.testcases:
            testcase.run()
            print("All tests completed")



if __name__ == "__main__":
    Tester = TestCases(app=Application)
    Tester.select_mode()
    Tester.run()
    Application()

