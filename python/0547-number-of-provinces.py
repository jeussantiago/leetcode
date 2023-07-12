class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        # same parent - part of same group
        if p1 == p2:
            return 0

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        - if its on the same row or col, the cities are connected

        [1,1,1,1]

        [[1,0,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,1,1]]

        n is the size of the matrix
        Time: O(n*n)
        Space: O(n)
        '''
        n = len(isConnected)
        uf = UnionFind(n)

        provinces = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    provinces -= uf.union(i, j)

        return provinces
