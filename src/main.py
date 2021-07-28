from serial_listener import SerialDataSource
from window import Window
from threading import Thread
import functools

if __name__ == "__main__":

    window = Window()
    window_thread = Thread(target=window._loop)

    def on_data(data):
        window.text = f"Distance: {data.strip()}cm"

    data_source = SerialDataSource()
    sock_thread = Thread(target=functools.partial(data_source.run, on_data))

    window_thread.start()
    sock_thread.start()

    window_thread.join()
