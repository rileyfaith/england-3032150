import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = min(
                (v for v in range(self.V) if not visited[v]),
                key=lambda v: dist[v], 
                default = None,
            )
            if u is None:
                break
            visited[u] = True


            for v in range(self.V):
                w = self.graph[u][v]
                if w and not visited[v] and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.print_dijkstra(dist)

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

    def prim(self):
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        # See the example output for expected result.
        parent = [None] * self.V
        key = [sys.maxsize] * self.V
        in_mst = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = min(
                (v for v in range(self.V) if not in_mst[v]),
                key=lambda v: key[v], 
                default = None,
            )
            if u is None:
                break
            in_mst[u] = True

            for v in range(self.V):
                w = self.graph[u][v]
                if w and not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
            
        self.print_prim(parent)

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")

    def kruskal(self):
        edges = [
            (u, v, self.graph[u][v])
            for u in range(self.V)
            for v in range(u + 1, self.V)
            if self.graph[u][v]
        ]
        edges.sort(key=lambda e: e[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = rx
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

            return True
        
        result = []
        for u, v, w in edges:
            if union(u, v):
                result.append((u, v, w))
                if len(result) == self.V - 1:
                    break
        self.print_kruskal(result)

    def print_kruskal(self, result):
        print("Edge \t Weight")
        # Note that the below code is slightly different than the Prim's.
        # You can change this print code according to your choice, but
        # you have to display your graph in (vertex->vertex weight) format.
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")


# Create a graph with 21 vertices.
graph = Graph(9)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 8)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 4, 9)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 0, 8)
graph.add_edge(7, 1, 11)
graph.add_edge(7, 8, 7)
graph.add_edge(8, 2, 2)
graph.add_edge(6, 8, 6)
graph.add_edge(5, 2, 4)
graph.add_edge(5, 3, 14)

print("TEST FOR PRIM")
graph.prim()
# The output should look like:
'''
0 -> 1 	 4
1 -> 2 	 8
2 -> 3 	 7
3 -> 4 	 9
2 -> 5 	 4
5 -> 6 	 2
6 -> 7 	 1
2 -> 8 	 2
'''

print("OTHER GRAPH TESTING")
# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
graph.kruskal()

# Example MST has the starting vertex as 0, but other vertex can also be chosen as the starting point. As the comsequence, different sets of edges may be involved in final MST.