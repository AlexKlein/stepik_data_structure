import sys


class Buffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self._buffer = []
        self._proc_unlock = 0
        self.log = []

    def enter(self, arrival, duration):
        if self._check(arrival):
            self._push(arrival, duration)
        else:
            self.log.append(-1)

    def _push(self, arrival, duration):
        if not self._buffer:
            time_exit = max(self._proc_unlock, arrival)
        else:
            time_exit = max(self._buffer[-1], arrival)
        self._buffer.append(time_exit + duration)
        self.log.append(time_exit)

    def _check(self, time_check):
        while self._buffer and time_check >= self._buffer[0]:
            self._proc_unlock = self._buffer.pop(0)
        if len(self._buffer) < self.max_size:
            return True
        return False


def get_source():
    size, count_of_pack = map(int, str(input()).split(' '))
    net_buffer = Buffer(size)

    for line in sys.stdin:
        arrival, duration = map(int, str(line.replace('\n', '')).split(' '))
        net_buffer.enter(arrival, duration)

    print(*net_buffer.log, sep='\n')


if __name__ == '__main__':
    get_source()
