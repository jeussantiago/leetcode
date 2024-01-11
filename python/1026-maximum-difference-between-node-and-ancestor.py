# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''
        - one pass where you pass the highest value node as the ancestor, then compare it with each child
        - another pass where you pass the lowest value node as the ancestor, then compare it with each child
        - solution is whichever number is bigger

        Time: O(n)
        Space: O(logn)
            ; (logn) recursion stack
        '''

        def getAncestorDiff(node, maxAncestor, minAncestor):
            if not node:
                return float('-inf')

            return max(
                getAncestorDiff(node.left, max(
                    node.val, maxAncestor), min(node.val, minAncestor)),
                getAncestorDiff(node.right, max(
                    node.val, maxAncestor), min(node.val, minAncestor)),
                abs(node.val - maxAncestor),
                abs(node.val - minAncestor)
            )

        return getAncestorDiff(root, root.val, root.val)
