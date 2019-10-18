class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity

    def get(self):
        pass
