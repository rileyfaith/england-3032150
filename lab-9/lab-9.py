from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def _validate(self, u, v):
        if not (0 <= u < self.vertices):
            raise IndexError(f"vertex {u} out of bounds")
        if v is not None and not (0 <= v < self.vertices):
            raise IndexError(f"vertex {v} out of bounds")
        
    def add_edge(self, u, v):
        self._validate(u, v)
        if v not in self.adjacency_list[u]:
            self.adjacency_list[u].append(v)
        if u not in self.adjacency_list[v]:
            self.adjacency_list[v].append(u)
        

    def dfs_shortest_path(self, start, end):
        self._validate(start,end)
        if start == end:
            return [start], 0
        
        parent = [-1] * self.vertices
        dist = [-1] * self.vertices
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in self.adjacency_list[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    if v == end:
                        q.clear()
                        break
                    q.append(v)
        
        if dist[end] == -1:
            return [], -1
        
        path = []
        cur = end
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        return path, dist[end]


    def bfs_shortest_path(self, start, end):
        self._validate(start, end)
        best_path = []
        visited = [False] * self.vertices

        def dfs(u, path):
            nonlocal best_path
            if best_path and len(path) >= len(best_path):
                return
            if u == end:
                best_path = path[:]
                return
            visited[u] = True
            for v in self.adjacency_list[u]:
                if not visited[v]:
                    path.append(v)
                    dfs(v, path)
                    path.pop()
            visited[u] = False
        dfs(start, [start])
        return (best_path, len(best_path) - 1) if best_path else ([], -1)

    def count_connected_components(self):
        visited = [False] * self.vertices
        count = 0

        for s in range(self.vertices):
            if not visited[s]:
                count += 1
                q = deque([s])
                visited[s] = True
                while q:
                    u = q.popleft()
                    for v in self.adjacency_list[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
        return count


    def is_bipartite(self):
        color = [-1] * self.vertices
        for s in range(self.vertices):
            if color[s] != -1:
                continue
            color[s] = 0
            q = deque([s])

            while q:
                u = q.popleft()
                for v in self.adjacency_list[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
                    
        return True

# Testing logic for the lab assignment

graph = Graph(20)

# Add edges to create a connected component and disconnected ones
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
graph.add_edge(15, 16)  
graph.add_edge(17, 18) 
graph.add_edge(10, 11)
graph.add_edge(11, 19)

### Test Case 1: Shortest Path

bfs_path, bfs_distance = graph.bfs_shortest_path(0, 19)
dfs_path, dfs_distance = graph.dfs_shortest_path(0, 19)

print(f"BFS Shortest Path from 0 to 19: {bfs_path} ")
print(f"BFS Shortest distance from 0 to 19: {bfs_distance}")

print(f"DFS Shortest Path from 0 to 19: {dfs_path}")
print(f"DFS Shortest distance from 0 to 19: {dfs_distance}")

### Test Case 2: Number of Connected Components

num_components = graph.count_connected_components()
print(f"Number of connected components in the graph: {num_components}")

### Test Case 3: Bipartite Check

is_bipartite = graph.is_bipartite()
print(f"Is the large graph bipartite? {'Yes' if is_bipartite else 'No'}")

# Create a graph for simpler testing
graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 2)
graph.add_edge(2, 5)

### Test Case 1: Shortest Path

bfs_path, bfs_distance = graph.bfs_shortest_path(0, 5)
dfs_path, dfs_distance = graph.dfs_shortest_path(0, 5)
print(f"BFS Shortest Path from 0 to 5: {bfs_path}")
print(f"BFS Shortest distance from 0 to 5: {bfs_distance}")

print(f"DFS Shortest Path from 0 to 5: {dfs_path}")
print(f"DFS Shortest distance from 0 to 5: {dfs_distance}")

### Test Case 2: Number of Connected Components

num_components = graph.count_connected_components()
print(f"Number of connected components in the graph: {num_components}")

### Test Case 3: Bipartite Check

is_bipartite = graph.is_bipartite()
print(f"Is the large graph bipartite? {'Yes' if is_bipartite else 'No'}")
