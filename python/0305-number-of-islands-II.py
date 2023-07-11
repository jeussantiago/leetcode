class Solution:

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        '''
        Union Find:

        - each added new islands is assumed to be an isloated islands
            - increase the count of number_of_islands += 1
        - if this island is connected to another island by not having the
        same parent
            - then decrease the number_of_islands -= 1
            - this still avois 3 islands that are completely seperatte and 3 
            points that are also connected, it would only depend on if the parents
            are different

        # T: O(k * log(m * n)) ; where k == positions.len
        # S: O(k + (m * n) ) ; k for the set of visited land positions and m*n for UnionFind parents and ranks
        '''
        # T: O(1)
        def isPosLand(row, col):
            if (
                0 <= row < m and
                0 <= col < n and
                (row, col) in landPos
            ):
                return True
            return False

        uf = UnionFind()
        landPos = set()
        res, number_of_islands = [], 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # T: O(k * 4 * log(m * n)) where k == positions.len
        # T: O(k * log(m * n))
        for row, col in positions:
            # some positions are duplicated, skip over the process for those but still add the island count (ex: [[0,0],[0,1],[1,2],[1,2]])
            if (row, col) not in landPos:
                landPos.add((row, col))
                number_of_islands += 1
                # T: O(4 * log(m * n))
                for next_row, next_col in neighbors:
                    if isPosLand(row + next_row, col + next_col):
                        node1 = (row, col)
                        node2 = (row + next_row, col + next_col)
                        # T: O(log(m * n))
                        if uf.union(node1, node2):
                            # two different islands coming together
                            number_of_islands -= 1

            res.append(number_of_islands)

        return res


class UnionFind:
    # T: O(1)
    # S: O(1)
    def __init__(self):
        self.parent = {}
        self.rank = collections.defaultdict(int)

    # T: O(log(m * n))
    # S: O(m * n)
    def find(self, node):
        father = self.parent.get(node, node)
        if node != father:
            self.parent[node] = self.find(father)
        return self.parent.get(node, node)

    # T: O(log(m * n))
    # S: O(m * n)
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            # islands already connected
            return 0

        if self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        # combined 2 different islands
        return 1
