class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def key(self) -> int:
        return self.value

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return TreeNode(key)
            if key < node.value:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        
        self.root = _insert(self.root, key)
        self._size += 1

    def search(self, key) -> TreeNode:
        cur = self.root
        while cur:
            if key == cur.value:
                return cur
            elif key < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return None


    def level_order_traversal(self) -> list:
        if not self.root:
            return []
        out, q = [], [self.root]
        while q:
            cur = q.pop(0)
            out.append(cur.value)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return out


# test
bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

assert bst._size == 7
assert bst.search(1) == None

bst.insert(1)
bst.insert(6)

assert bst._size == 9
assert bst.search(1).key == 1

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(1)
bst.insert(6)

assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]

