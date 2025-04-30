class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    def empty(self):
        return self.size == 0
    
    def get_size(self) -> int:
        return self.size

    def push_front(self, data):
        new_node = Node(data)
        if self.front is None and self.size == 0:
            self.front = self.back = new_node
            self.size = 1
            return
        cur = self.front
        new_node.next = cur
        cur.prev = new_node
        self.front = new_node
        self.size += 1

    def push(self, data):
        new_node = Node(data)
        if self.back is None and self.size == 0:
            self.front = self.back = new_node
            self.size = 1
            return
        cur = self.back
        cur.next = new_node
        new_node.prev = cur
        self.back = new_node
        self.size += 1

    def pop_front(self) -> int:
        if self.size == 0:
            return None
        
        if self.size == 1:
            pop_node = self.front
            self.front = self.back = None
            self.size = 0
            return pop_node.item

        pop_node = self.front
        new_front = pop_node.next
        new_front.prev = None
        pop_node.next = None
        self.front = new_front
        self.size -= 1
        return pop_node.item
    
    def pop(self) -> int:
        if self.size == 0:
            return None
        
        if self.size == 1:
            pop_node = self.back
            self.front = self.back = None
            self.size = 0
            return pop_node.item

        pop_node = self.back
        new_back = pop_node.prev
        new_back.next = None
        pop_node.prev = None
        self.back = new_back
        self.size -= 1
        return pop_node.item
    
    def peek_front(self) -> int:
        return self.front.item
    
    def peek_back(self) -> int:
        return self.back.item



def isPalindrome(s: str) -> bool:
    deque = Deque()
    
    for ch in s:
        deque.push(ch)

    while not deque.empty():
        if deque.pop_front() != deque.pop():
            return False
    return True
        
def reverse_deque(deque):
    reversed_deque = Deque()
    cur = deque.back
    while cur is not None:
        reversed_deque.push(cur.item)
        cur = cur.prev
    return reversed_deque

if __name__ == '__main__':
    deque = Deque()
    deque.push(1)
    deque.push(2)
    deque.push(3)

    reversed_deque = reverse_deque(deque)
    while not reversed_deque.empty():
        print(reversed_deque.pop_front())  # Should output 3, 2, 1.