class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        def _put(node, key, value):
            if node is None:
                return TreeNode(key, value)
            if key < node.key:
                node.left = _put(node.left, key, value)
            elif key > node.key:
                node.right = _put(node.right, key, value)
            else:
                node.value = value
            return node
        
        self.root = _put(self.root, key, value)
        
    def get(self, key):
        def _get(node, key):
            if node is None:
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return _get(node.left, key)
            else:
                return _get(node.right, key)
            
        return _get(self.root, key)
    

# tests
tree_map = TreeMap()

# Test putting and getting key-value pairs.
tree_map.put(3, "A")
tree_map.put(1, "B")
tree_map.put(2, "C")
tree_map.put(4, "D")

assert tree_map.get(2) == "C"
assert tree_map.get(1) == "B"
assert tree_map.get(4) == "D"
# Non-existent key should return None.
assert tree_map.get(5) is None