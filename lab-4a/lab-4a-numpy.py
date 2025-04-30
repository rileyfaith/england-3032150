import numpy as np

class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = -1
        self.back = -1
        self.size = 0
        self.array = np.zeros(self.capacity, dtype=object)

    def empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def full(self):
        return self.size == self.capacity
    
    def push_front(self, data):
        if self.full:
            raise OverflowError('deque is full')
        
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.array[self.front] = data
        self.size += 1

    def push(self, data):
        if self.full:
            raise OverflowError('deque is full')
        
        self.array[self.back] = data
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def pop_front(self):
        if self.empty():
            raise IndexError("deque is empty")
        
        value = self.array[self.front]
        self.array[self.front] = 0
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def pop(self):
        if self.empty():
            raise IndexError("deque is empty")
        
        self.back = (self.back - 1 + self.capacity) % self.capacity
        value = self.array[self.back]
        self.array[self.back] = 0
        self.size -= 1
        return value

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = np.zeros(new_capacity, dtype=object)

        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]
        
        self.front = 0
        self.back = self.size
        self.capacity = new_capacity
        self.array = new_array

