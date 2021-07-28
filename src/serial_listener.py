import serial
import struct

class SerialDataSource:
    def __init__(self):
        self._serial = serial.Serial("COM3", 9600)
    
    def run(self, on_data):
        while True:
            line = self._serial.readline(20).decode("utf-8")
            if not line:
                return
            on_data(line)
