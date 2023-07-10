# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n) still need to go through all nodes of binary tree to figure out max depth
        Space: O(1) keep track of the level and current node (doesn't include the current tree)
        '''

        def helper(node, level):
            if not node:
                return level

            return max(
                helper(node.left, level+1),
                helper(node.right, level+1)
            )

        res = helper(root, 0)
        return res
