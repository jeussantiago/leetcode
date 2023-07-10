# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.


        Time: O(n)
        Space: O(n) n is the height of the tree
        """

        def helper(node):
            if not node:
                return

            left_node = helper(node.left)
            right_node = helper(node.right)

            if left_node:
                last_left_node = left_node
                while last_left_node.right:
                    last_left_node = last_left_node.right

                last_left_node.right = right_node
                node.right = left_node
                node.left = None

            return node

        helper(root)
