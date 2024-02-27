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


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> list:
        '''
        follow up question
        - return the path/array which has the longest_path
        '''
        longest_path = [root.val]

        def dfs(node):
            nonlocal longest_path
            if not node:
                return []

            left, right = dfs(node.left), dfs(node.right)

            possible_new_longest_path = left + [node.val] + right

            if len(possible_new_longest_path) > len(longest_path):
                longest_path = possible_new_longest_path

            if len(left) >= len(right):
                return left + [node.val]

            return [node.val] + right

        dfs(root)
        return longest_path
