# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''
        res = []

        def dfs(node):
            if not node:
                return

            res.append(str(node.val))

            # do left side
            res.append('(')
            dfs(node.left)
            res.append(')')

            if node.right:
                # do right side
                res.append('(')
                dfs(node.right)
                res.append(')')
            elif not node.left:
                # if right side doesn't exist
                # remove the left side if its empty
                res.pop()
                res.pop()

        dfs(root)
        return "".join(res)
