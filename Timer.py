import time


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self._time_pointer = time.time()
        self._times = list()

    def set_time(self, save_time=False):
        res = time.time()
        if save_time:
            self._times.append(res)
        self._time_pointer = res

    def time_since_set(self, save_time=False):
        res = time.time() - self._time_pointer
        if save_time:
            self._times.append(res)
        return res

    def time_since_start(self, save_time=False):
        res = time.time() - self.start_time
        if save_time:
            self._times.append(res)
        return res
