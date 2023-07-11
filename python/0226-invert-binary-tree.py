# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def helper(node, replicateNode):
            if not node:
                return

            replicateNode.val = node.val

            if node.left:
                replicateNode.right = TreeNode()
                helper(node.left, replicateNode.right)

            if node.right:
                replicateNode.left = TreeNode()
                helper(node.right, replicateNode.left)

            return replicateNode

        return helper(root, TreeNode())
