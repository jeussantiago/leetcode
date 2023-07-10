# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(n)
        '''

        def helper(node, level):
            if not node:
                return

            if level == len(res):
                res.insert(0, [])

            res[len(res) - 1 - level].append(node.val)

            helper(node.left, level+1)
            helper(node.right, level+1)

        res = []
        helper(root, 0)
        return res
