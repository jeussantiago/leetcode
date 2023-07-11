# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        def dfs(node):
            if not node.left:
                return node

            new_root = dfs(node.left)

            # set the new root and it's children
            tmp = node.left
            tmp.left = node.right
            tmp.right = node

            # remove the children of the previous root
            node.left = None
            node.right = None

            return new_root

        return dfs(root)
