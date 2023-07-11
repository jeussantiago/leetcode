class treeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        preorder = preorder.split(',')
        N = len(preorder)
        self.i = 0

        def dfs():
            if self.i >= N:
                self.i = float('inf')
                return None

            if preorder[self.i] == "#":
                self.i += 1
                return None

            node = treeNode(preorder[self.i])
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        dfs()
        return self.i == N
