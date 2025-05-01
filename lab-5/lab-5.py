class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.vertex = [i for i in range(size)]
        self.weight = [1] * size
        self.count = size
        self.rank = [0] * size

    def validate(self, v1):
        if not (0 <= v1 < len(self.parent)):
            return False
        return True

    def size(self, v1):
        root = self.find(v1)
        return self.weight[root]

    def parent_of(self, v1):
        self.validate(v1)
        return self.parent[v1]

    def isConnected(self, v1, v2) -> bool:
        return self.find(v1) == self.find(v2)

    def find(self, v1):
        self.validate(v1)
        while v1 != self.parent[v1]:
            self.parent[v1] = self.parent[self.parent[v1]]
            v1 = self.parent[v1]
        return v1



    def unionbyweight(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return
        if self.weight[r1] < self.weight[r2]:
            r1, r2 = r2, r1
        self.parent[r2] = r1
        self.weight[r1] += self.weight[r2]
        self.count -= 1


    def unionbyrank(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return
        if self.weight[r1] < self.weight[r2]:
            r1, r2 = r2, r1
        self.parent[r2] = r1
        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1
        self.weight[r1] += self.weight[r2]
        self.count -= 1

    def joinBlocks(self, Connected):
        for edge in Connected:
            try:
                u, v = edge[:2]        # grab the first two fields only
            except ValueError:
                raise ValueError("Each entry in 'connections' must contain ≥2 items")
            self.unionbyweight(u, v)

    def findBlockSets(self):
        block = {}
        for v in range(len(self.parent)):
            root = self.find(v)
            block.setdefault(root, []).append(v)
        return block

    def findBlockCount(self, blockid):
        return self.size(blockid)



if __name__ == '__main__':
    # Tasks A
    uf = DisjointSet(10)
    # 0 1-2-5-6-7 3-8-9 4
    uf.unionbyrank(1, 2)
    uf.unionbyrank(2, 5)
    uf.unionbyrank(5, 6)
    uf.unionbyweight(6, 7)
    uf.unionbyrank(3, 8)
    uf.unionbyweight(8, 9)
    print(uf.isConnected(1, 5))  # true
    print(uf.isConnected(5, 7))  # true
    print(uf.isConnected(4, 9))  # false
    # 0 1-2-5-6-7 3-8-9-4
    uf.unionbyweight(9, 4)
    print(uf.isConnected(4, 9))  # true

    # Tasks B
    Connected = [[1,1,0,1], [1,1,0,0], [0,0,1,1], [1,0,1,1]]
    uf = DisjointSet(4)
    uf.joinBlocks(Connected)
    uf.findBlockCount(1)