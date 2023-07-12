# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        Space optimization
            - space complexity doesnt change
            - but avg space complexity is reduced
        Time: O(n)
        Space: O(n)
        '''
        self.prev = None
        self.minDiff = float('inf')

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if self.prev != None:
                self.minDiff = min(self.minDiff, node.val - self.prev)
            self.prev = node.val

            dfs(node.right)

        dfs(root)
        return self.minDiff


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        order = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            order.append(node.val)
            dfs(node.right)

        dfs(root)
        minDiff = float('inf')
        for i in range(1, len(order)):
            minDiff = min(minDiff, order[i] - order[i-1])

        return minDiff
