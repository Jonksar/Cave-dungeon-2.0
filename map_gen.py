import itertools
import random


class CellularAutomaton:
    def __init__(self, size=128, rule1=4, rule2=4, percent_filled=50):
        self.size = size
        self.rule1 = rule1
        self.rule2 = rule2
        self.map = [[1 if percent_filled > random.randint(0, 100) else 0 for i in range(size)] for j in range(size)]

    def iter(self):
        res = [[0 for _ in range(self.size)] for __ in range(self.size)]

        for x, y in itertools.product(range(self.size), repeat=2):

            if self.map[y][x]:
                if self.count_filled(x, y) > self.rule1:
                    res[y][x] = 1
                else:
                    res[y][x] = 0
            else:
                if self.count_filled(x, y) > self.rule2:
                    if self.count_filled(x, y) > self.rule2:
                        res[y][x] = 1
                    else:
                        res[y][x] = 0

        self.map = res

    def count_filled(self, x, y):
        counter = 0
        for dx, dy in itertools.product([-1, 0, 1], repeat=2):
            try:
                if self.map[y + dy][x + dx]:
                    counter += 1

            except: pass

        return counter

    def __call__(self):
        for _ in range(10):
            self.iter()

    def __str__(self):
        fun = lambda x: "#" if x == 1 else " "
        return "\n".join([''.join(map(fun, l)) for l in self.map])

    def return_value(self, x1, x2, y):
        if y < 0 or y >= self.size:
            return [0 for i in range(x2 - x1)]

        elif x1 < 0:
            return [0 for i in range(0 - x1)] + self.map[y][:x2]

        elif x2 >= self.size:
            return self.map[y][x1:] + [0 for i in range(x2 - (self.size - 1))]

        else:
            return self.map[y][x1:x2]
