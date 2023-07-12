# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n)
        Space: O(logn)
        '''
        res = [0]

        def dfs(node, cnt, isRightChild):
            if not node:
                return 0

            res[0] = max(res[0], cnt)

            if isRightChild:
                dfs(node.left, cnt + 1, False)
                dfs(node.right, 1, True)
            else:
                dfs(node.left, 1, False)
                dfs(node.right, cnt + 1, True)

        dfs(root.left, 1, False)
        dfs(root.right, 1, True)

        return res[0]
