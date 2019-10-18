class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current == self.capacity:
            self.current = 0

        self.storage[self.current] = item
        self.current += 1

    def get(self):
        return [value for value in self.storage if value is not None]
