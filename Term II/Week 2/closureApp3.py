class Averager:
    def __init__(self):
        self.values = []
        self._count = 0
        self._total = 0

    def add(self, value):
        self.values.append(value)
        self._total += value
        self._count += 1
        return self._total / self._count


def averager():
    total = 0
    count = 0

    def add(value):
        nonlocal total, count
        total += value
        count += 1
        return 0 if count == 0 else total/count
    return add