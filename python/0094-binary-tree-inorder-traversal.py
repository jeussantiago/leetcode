# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        [1,null,2,3]
                1
         null       2
                  3    null

        in-order (left, n, right): 1, 3, 2


        Time: O(n) cause you have to visit evrey node
        Space: O(1)
        '''
        res = []

        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)

        helper(root)
        return res
