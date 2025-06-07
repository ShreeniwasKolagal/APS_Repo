class UnionFind:
    def __init__(self, n):
        # parent[i] < 0 indicates that i is a root with size == -parent[i]
        self.parent = [-1] * n

    def find(self, x):
        # path compression
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # union by size (attach smaller tree to larger)
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if -self.parent[rx] < -self.parent[ry]:
            rx, ry = ry, rx
        # now root rx has larger size
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx
        return True

    def size(self, x):
        return -self.parent[self.find(x)]


# Example usage:
uf = UnionFind(5)  # elements 0..4
uf.union(0, 1)
uf.union(2, 3)
print(uf.find(0), uf.find(1))  # both belong to the same set (root)
print(uf.find(2), uf.find(3))
uf.union(1, 2)
print(uf.size(3))  # size of the merged set {0,1,2,3} => 4
