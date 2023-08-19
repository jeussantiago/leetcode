class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1):
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        Minimum Spanning Tree(MST): a graph where all the nodes are connected with the minimum possible edges

        1 - 2       1 - 2
        |   |   =>      |
        3 - 4       3 - 4

        Kruskal's algorithm
        - sort all the edges of a graph in increasing order
        - keep ading a new edges and nodes in the MST if the newly added edge does not form a cycle
        - picks the minimum weighted edge first


        - We run this algorithm to find the MST of the original graph and keep track of it's original weight
        - Brute Force: We go one by one for each node to not include it into the MST and run the algorithm again
            (whats the weight of MST without node 1)
            (whats the weight of MST without node 2, etc.)


        - Node is critical (add all connecting edges to critical edge result)
            - if the weight is greater than orignal weight
            - the number of nodes in the MST != n (can just check max value in rank - if all part of same graph, all nodes get added to one node and total should equal n)

        ** if an edge is critical, it cannot be psuedo-critical b/c critical edges have to appear in all MSTs

        - if an edge is not critical, test if its pseudo-critical
        pseudo-critical: we forcibly include the edge into the tree and it's still possible to create an MST like the original

        - so if there is an edge that connects one node to the rest of the graph, it would be a critical edge. Since its a critical edge, we would never test if the edge is a psuedo critical(by forcing it into the graph)
            - this is why we don't check the number of nodes in the graph because we can gurantee that all nodes are connected so a MST is created

        E is the number of edges
        Time: O(E^2)
            ;(1) union find operations
            ;(E) find original MST weight
            ;(E^2) find MST weight excluding each edge
        Space: O(n)
            ; (n) Union find rank and parent list
        '''

        for i, edge in enumerate(edges):
            edge.append(i)  # [v1, v2, weight, original_index]

        edges.sort(key=lambda x: x[2])

        mst_weight = 0
        uf = UnionFind(n)
        for n1, n2, w, _ in edges:
            if uf.union(n1, n2):
                mst_weight += w

        critical, pseudo = [], []
        for v1, v2, e_weight, i in edges:
            # Try without curr edge
            weight = 0
            uf = UnionFind(n)
            for n1, n2, w, j in edges:
                if i != j and uf.union(n1, n2):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            # Try with curr edge
            uf = UnionFind(n)
            uf.union(v1, v2)
            weight = e_weight
            for n1, n2, w, j in edges:
                if uf.union(n1, n2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
