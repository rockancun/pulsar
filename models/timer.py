import logging
import threading
import ctypes
import time


class Timer(threading.Thread):

    def __init__(self, event):
        threading.Thread.__init__(self)
        self.__event = event
        self.__seconds = 0.5

    def run(self):
        try:
            while True:
                self.__event()
                time.sleep(self.get_seconds())
        finally:
            print('exit')

    def stop(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            thread_id,
            ctypes.py_object(SystemExit))

        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def set_seconds(self, seconds):
        self.__seconds = seconds

    def get_seconds(self):
        return self.__seconds
