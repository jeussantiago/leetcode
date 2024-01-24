# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n)
            ; (n) go through all nodes in tree
            ; (1) decide if path is a palindrome 
            ;   (hash map will only have values 1-9)
        Space: O(logn)
            ; (logn) resucrsion stack
            ; (1) hash map size with only values 1-9
        '''

        cnt = collections.defaultdict(int)

        def isPalindrome():
            num_odd = 0
            for val in cnt.values():
                # odd
                if val % 2 == 1:
                    num_odd += 1

            return True if num_odd <= 1 else False

        def dfs(node):
            if not node:
                return 0

            cnt[node.val] += 1

            if not node.left and not node.right:
                is_path_palindrome = 1 if isPalindrome() else 0
                cnt[node.val] -= 1
                return is_path_palindrome

            num_pseudo = dfs(node.left) + dfs(node.right)
            cnt[node.val] -= 1

            return num_pseudo

        return dfs(root)
