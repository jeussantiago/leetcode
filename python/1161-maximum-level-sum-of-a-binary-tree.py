# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        - keep track of:
            - the max sum
            - the level with the max sum (return value)

        Time: O(n)
        Space: O(1)
        '''

        res = 0
        max_total_level = float('-inf')
        level = 1
        q = collections.deque([root])
        while q:
            level_total = 0
            for _ in range(len(q)):
                node = q.pop()
                level_total += node.val

                if node.left:
                    q.appendleft(node.left)

                if node.right:
                    q.appendleft(node.right)

            if level_total > max_total_level:
                max_total_level = level_total
                res = level

            level += 1

        return res
