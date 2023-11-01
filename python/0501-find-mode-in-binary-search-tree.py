# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        '''
        no extra space (ignoring recursion stack and result space)

        in-order traversal

        - increase a the current streak for the node value
            - reset if different number
        - if current streak > max streak
            - start new res
            - set new max_streak

        - if the current streak for the number is the same
            - add the number to the 


        Time: O(n)
        Space: O(1)
        '''
        max_streak, curr_streak, curr_num = 0, 0, 0
        res = []

        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, res
            if not node:
                return

            dfs(node.left)
            # check if continue streak or not
            if node.val == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = node.val

            if curr_streak > max_streak:
                res = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                res.append(node.val)

            dfs(node.right)

        dfs(root)
        return res


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        '''
        hashmap

        Time: O(n)
        Space: O(n)
        '''
        def dfs(node):
            if not node:
                return

            count[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        count = collections.defaultdict(int)
        dfs(root)

        max_freq = max(count.values())
        res = [key for key, val in count.items() if val == max_freq]
        return res
