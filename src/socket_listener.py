import socket
import struct

class SocketDataSource:
    def __init__(self, addr, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((addr, port))
    
    def run(self, on_data, fmt):
        data_size = struct.calcsize(fmt)
        while True:
            buffer = self._sock.recv(data_size)
            if len(buffer) < data_size:
                return
            data = struct.unpack(fmt, buffer)
            on_data(*data)
