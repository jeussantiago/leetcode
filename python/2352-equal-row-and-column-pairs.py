class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0


class Trie:
    def __init__(self, grid):
        self.root = TrieNode()
        self.grid = grid

    def insert(self, col):
        node = self.root
        for row in range(len(self.grid)):
            if self.grid[row][col] not in node.children:
                node.children[self.grid[row][col]] = TrieNode()

            node = node.children[self.grid[row][col]]

        node.frequency += 1

    def search(self, row):
        node = self.root
        for col in range(len(self.grid)):
            if self.grid[row][col] not in node.children:
                return 0

            node = node.children[self.grid[row][col]]

        return node.frequency


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        [3,1,2,2]
        [1,4,4,4]
        [2,4,2,2]
        [2,4,2,2]
        frequency=6

        Time: O(n^2)
        Space: O(n^2)
        '''

        root = Trie(grid)
        n = len(grid)
        for col in range(n):
            root.insert(col)

        res = 0
        for row in range(n):
            res += root.search(row)

        return res
