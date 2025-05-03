class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self) -> list:
        result = []
        def _pre(node):
            if node is None:
                return
            result.append(node.value)
            _pre(node.left)
            _pre(node.right)
        
        _pre(self.root)
        return result


    def inorder_traversal(self) -> list:
        result = []

        def _in(node):
            if node is None:
                return
            _in(node.left)
            result.append(node.value)
            _in(node.right)

        _in(self.root)
        return result

    def postorder_traversal(self) -> list:
        result = []
        
        def _post(node):
            if node is None:
                return 
            _post(node.left)
            _post(node.right)
            result.append(node.value)

        _post(self.root)
        return result



class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if u < 0 or u >= self.vertices or v < 0 or v >= self.vertices:
            raise IndexError("vertex index out of range")
        self.adjacency_list[u].append(v)

    def dfs(self, source):
        if source < 0 or source >= self.vertices:
            raise IndexError("source vertex out of range")
        visited = [False] * self.vertices
        order = []

        def _dfs(v:int):
            visited[v] = True
            order.append(v)
            for nbr in self.adjacency_list[v]:
                if not visited[nbr]:
                    _dfs(nbr)
        
        _dfs(source)
        return order
        

    def bfs(self, source):
        if source < 0 or source >= self.vertices:
            raise IndexError("source vertex out of range")
        from collections import deque

        visited = [False] * self.vertices
        order = []
        q = deque([source])
        visited[source] = True

        while q:
            v = q.popleft()
            order.append(v)
            for nbr in self.adjacency_list[v]:
                if not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)
        return order

# Create a binary tree
bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)
bt.root.left.left.left = TreeNode(8)
bt.root.left.left.right = TreeNode(9)
bt.root.right.right.right = TreeNode(10)

# Test the traversals
print("Preorder Traversal:", bt.preorder_traversal())
print("Inorder Traversal:", bt.inorder_traversal())    
print("Postorder Traversal:", bt.postorder_traversal())  



# Create a graph with 20 vertices
graph = Graph(20)

# Add edges (change as needed)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(4, 9)
graph.add_edge(4, 10)
graph.add_edge(5, 11)
graph.add_edge(5, 12)
graph.add_edge(6, 13)
graph.add_edge(6, 14)
graph.add_edge(7, 15)
graph.add_edge(7, 16)
graph.add_edge(8, 17)
graph.add_edge(8, 18)
graph.add_edge(9, 19)

# Test DFS and BFS from a source vertex
print("DFS from vertex 0:", graph.dfs(0))  
print("BFS from vertex 0:", graph.bfs(0))

# Create a graph with 4 vertices
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Test DFS and BFS from a source vertex
print("DFS from vertex 2:", graph.dfs(2))
print("BFS from vertex 2:", graph.bfs(2)) 