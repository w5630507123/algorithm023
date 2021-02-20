class UnionFind:
    """并查集
    """

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # 初始连通分量数为 n 个
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        # 合并，连通分量数减少
        if u_root != v_root:
            self.parent[u_root] = v_root
            self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    # 有相连关系，则进行合并
                    uf.union(i, j)
        return uf.count