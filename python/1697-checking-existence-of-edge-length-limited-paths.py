class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node):
        if node != self.group[node]:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1, node2):
        group1, group2 = self.find(node1), self.find(node2)

        if group1 == group2:
            return

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = self.group[group1]
            self.rank[group1] += self.rank[group2]
        else:
            self.group[group1] = self.group[group2]
            self.rank[group2] += self.rank[group1]

    def is_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        - sort the edge_list by the distance
            - b/c we don't want to categorize anything greater than the limit since theres no point in that. Anything greater is the same thing as having no edge
        - in the same sense we can sort query_list since we want to do the shorted limits first
            - will need to keep track of the original index for the results order

        - by sorting these two, it alleviates the issue of  trying to find a path with less than the limit.
            - cause a union find group is created if the distance < limit
            - if there is no connetion between one point and another, it means that there is no edge that connects or that the distance is just too big for the limit
            - since everything in the current union groups has a distance < limit, you can confidently just check if a node belongs to a specific group or not
            - being in that group means there is a connection with distance < limit, otherwise not

        e is the number of edges
        q is the number of qqueries
        Time: O(n + eloge + qlogq)   
                    ; (n) initializing the unionfind group and rank arrays
                    ; (eloge) sorting of edge_list
                    ; (qlogq) sorting of queries
                    ; (q + e) going through all the queries and going through all the edges with distance < limit - at worst will do 1 loop, thats why it's "+"
                    ;           - (1) adding edges to union group
                    ;           - (1) checking if node p and node q and connected - unionfind.find()
        Space: O(2n + q + q + e)
                    ; (2n) group and rank arrays for unionfind
                    ; (q) results array
                    ; (q) query_list python sorting
                    ; (e) edge_list python sorting
            : O(n + q + e)
        '''
        Q = len(queries)
        uf = UnionFind(n)
        res = [False] * Q
        # store original index of queries
        for i in range(Q):
            queries[i].append(i)

        # sort edge_list by distance
        edge_list.sort(key=lambda x: x[2])
        # sort queries by limit
        queries.sort(key=lambda x: x[2])

        # add edges from edge_list to group if distance < limit
        edge_list_ind = 0
        for p, q, limit, original_ind in queries:
            # distance < limit
            while edge_list_ind < len(edge_list) and edge_list[edge_list_ind][2] < limit:
                node1, node2 = edge_list[edge_list_ind][0], edge_list[edge_list_ind][1]
                uf.join(node1, node2)
                edge_list_ind += 1

            # check if node p and node q are connected
            res[original_ind] = uf.is_connected(p, q)

        return res
