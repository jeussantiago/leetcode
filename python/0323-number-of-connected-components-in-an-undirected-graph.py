class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Union Find:

        n = 5, edges = [[0,1],[2,3],[3,1],[4,1]]

        parents = [0,1,2,3,4]
        rank    = [1,1,1,1,1]

        - 0 and 1's parents are index 0 and 1 respectively
            (this means that they are not connected, but we need to connect them)
            - if they have the same rank, make one of them the parent by setting the parent index of the other edge
            - increase the rank of the parent by the rank of the other
        parents = [0,0,2,3,4]
        rank    = [2,1,1,1,1]   

        - similar case for edge [3,1]
        parents = [0,0,2,2,4]
        rank    = [2,1,2,1,1] 

        - edge [3,1]
            - we know for this one that 3 has a parent so we need to go to the 
            parent of that until we have reached the end 3 -> 2 -> 2
            - parent of 1 is 0

            - they have the same rank, so just make one of them the parent
                - update the parent of 3
                - don't touch 0, since it is the parent
                - increase the rank of 0
                (so if we were given index 3 to find its parent, the path would be: 3 -> 2 -> 0 -> 0)
                ===> update the parents of children if they are not looking at the right parent already
                    - hear make 3's parent 0 instead of 2
                    - this will avoid issues down the line of big linked list
        parents = [0,0,0,0,4]
        rank    = [3,1,2,1,1] 

        - edge [4,1]
            - parent of 4 is 4
            - parent of 1 is 0

            - 0 rank > 4 rank
            - 4 becomes a child of 0
            - update 4 parent, increase 0 rank
        parents = [0,0,0,0,0]
        rank    = [4,1,2,1,1] 


        ** if the parents are the same,
        - so if we were given edge [1,2]
            - we would see that they both have 0 as a parent, which means that they are already connected
            - we don't want to do anything => don't increase 0 rank or change anyones parent
        ** in this case the number of groups also doesn't change
        ** the number of groups change if the parents are different since 2 groups are joining together, we can subtrack by 1
        *** increase rank by the rank of the other node, this will make sure that the parent rank includes the number of nodes in the other component


        Time: O(nlogn) ; find() is (logn) ; union() is (logn) b/c it calls find()
        Space: O(n) for storing the parent and ranks
        '''
        uf = UnionFind(n)
        res = n
        for node1, node2 in edges:
            if uf.union(node1, node2):
                # seperate nodes/groups were disconnected
                res -= 1

        return res


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    # finds the parent of the node
    def find(self, node):

        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            # nodes are already connected
            return 0

        # nodes are disconnected, different parents
        if self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]

        return 1
