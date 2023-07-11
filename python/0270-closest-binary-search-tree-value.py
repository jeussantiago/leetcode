# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        '''
        - if the current node is bigger than the target
            - go left
        - if the current node is smaller than the target
            - go right

        Time: O(h) where h is the height of the tree
        Space: O(1)
        '''
        res = [None, float('inf')]

        def helper(node, target):
            if not node:
                return

            node_diff = abs(node.val - target)
            if node_diff < res[1]:
                res[0] = node.val
                res[1] = node_diff

            if target < node.val:
                helper(node.left, target)
            if target > node.val:
                helper(node.right, target)

        helper(root, target)
        return res[0]
