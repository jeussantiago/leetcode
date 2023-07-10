# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(node, rootLeafDigits):

            if not node:
                return

            if not node.left and not node.right:
                # leaf node - add number to res
                nonlocal res
                res += int(rootLeafDigits + str(node.val))
                return

            # traverse until you get to leaf node
            helper(node.left, rootLeafDigits + str(node.val))
            helper(node.right, rootLeafDigits + str(node.val))

        helper(root, "")
        return res
