import random
from Timer import Timer
import itertools
import math


def interpolate(v0, v1, t):
    t = min(1, max(0, t))

    if isinstance(v0, tuple) or isinstance(v0, list):
        t = math.sqrt(t)
        return tuple(((1-t)*v0[i] + t*v1[i] for i in range(len(v0))))

    elif isinstance(v0, int):
        return round((1-t)*v0 + t*v1)

    elif isinstance(v0, float):
        return (1 - t) * v0 + t * v1


def gen_colors(size, col='fire'):
    # HASHTAG PROCEDURAL GENERATION IS LIFE
    if col == 'fire':
        res = [(200 + random.randint(0, 55), 0 + random.randint(0, 30), 0 + random.randint(0, 30)) for i in range(size)]
    elif col == 'ice':
        res = []

        for i in range(size):
            x = random.randint(-50, 50)
            y = random.randint(0, 50)
            res.append((100 + x, 100 + x, 200 + y))

    if size == 1:
        return res[0]
    else:
        return res


class Buff:
    def __init__(self):
        NotImplementedError()

    def __call__(self, player):
        # used to do the effects on character
        NotImplementedError()

    def update(self, *args, **kwargs):
        # update the buff at every frame
        NotImplementedError()


class FireBuff(Buff):
    def __init__(self, duration=3):
        super(Buff, self).__init__()

        # Times
        self.max_duration = duration
        self.timer = Timer()

        # Colors are nice
        self.start_color = (255 - random.randint(0, 25), 255 - random.randint(0, 25), 25 - random.randint(0, 25))
        self.middle_color = ()
        self.end_color = (255 - random.randint(0, 25), 0 + random.randint(0, 25), 0 + random.randint(0, 25))
        self.cur_color = self.start_color

    def __call__(self, player):
        pass

    def update(self, *args, **kwargs):
        self.cur_color = interpolate(self.start_color, self.end_color,
                                     self.timer.time_since_start() / float(self.max_duration))


class IceBuff(Buff):
    def __init__(self, duration, slow_amount = 0.45):
        super(Buff, self).__init__()

        # Times
        self.max_duration = duration
        self.timer = Timer()

        # Colors are nice
        self.color = gen_colors(1, col='ice')

        # properties
        self.slow_amount = slow_amount

    def __call__(self, player):
        pass

    def update(self, *args, **kwargs):
        # If time lived > maximum lifetime
        if self.timer.time_since_start() >= self.max_duration:
            # Suicide
            kwargs['buff_list'].remove(self)
            del self
