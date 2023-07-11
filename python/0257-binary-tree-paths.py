# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(node, lst):
            if not node.left and not node.right:
                path = "->".join(lst + [str(node.val)])
                res.append(path)
            if node.left:
                helper(node.left, lst + [str(node.val)])
            if node.right:
                helper(node.right, lst + [str(node.val)])

        helper(root, [])
        return res
