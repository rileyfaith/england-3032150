class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item # int
            self.next = next_node # IntNode
            
    def __init__(self):
        self.first = None # initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    def insert(self, item, position):
        new_node = self.IntNode(item, None)
        if self.first is None:
            self.first = new_node
            return
        
        if position == 0:
            new_node.next = self.first
            self.first = new_node
            return
        
        cur = self.first
        index = 0
        while cur.next is not None and index < position - 1:
            cur = cur.next
            index += 1
        
        new_node.next = cur.next
        cur.next = new_node

    def reverse(self):
        if self.first is None or self.first.next is None:
            return self.first
        
        cur = self.first
        prev = None
        while cur is not None:
            nextt = cur.next

            cur.next = prev

            prev = cur
            cur = nextt
        
        self.first = prev
        return prev


    def replicate(self):

        if self.first is None:
            return
        
        replicated = SLList()
        cur = self.first
        recent = None

        while cur is not None:
            for _ in range(cur.item):
                dupe = self.IntNode(cur.item, None)
                if replicated.first is None:
                    replicated.first = dupe
                    recent = dupe
                else:
                    recent.next = dupe
                    recent = dupe
            cur = cur.next
        return replicated
        
    def equals(self, anotherList):
        if self.first is None and anotherList.first is None:
            return True
        
        cur = self.first
        cur2 = anotherList.first
        while cur is not None and cur2 is not None:
            if cur.item != cur2.item:
                return False
            else:
                cur = cur.next
                cur2 = cur2.next
        if cur is not None or cur2 is not None:
            return False
        return True
        


if __name__ == '__main__':
    L = SLList()
    L.addFirst(15)
    L.addFirst(10)
    L.addFirst(5)
    L.reverse()

    L_expect = SLList()
    L_expect.addFirst(5)
    L_expect.addFirst(10)
    L_expect.addFirst(15)	

    if L.equals(L_expect):
        print("Two lists are equal, tests passed")
    else:
        print("Two lists are not equal, tests failed")

