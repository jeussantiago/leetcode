# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        longest_path = 1

        def dfs(node):
            nonlocal longest_path

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            longest_path = max(longest_path, left + right + 1)

            return max(left, right) + 1

        dfs(root)

        return longest_path - 1
