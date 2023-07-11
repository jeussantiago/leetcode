# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        '''
        - do need to visit every node
        - can't do this in O(h) time
        - reason: 2 might continue the longest consecutive sequence if there was a 2->8->9->10->11

        - keep track of the previous number
        - if current number == previous_number + 1
            - go to next recursion with count += 1
        else:
            - go to next recursion with count = 1

        '''
        def dfs(node, previous_val, consec_counter):
            if not node:
                return 0

            if node.val == previous_val + 1:
                consec_counter += 1
            else:
                consec_counter = 1

            left = dfs(node.left, node.val, consec_counter)
            right = dfs(node.right, node.val, consec_counter)

            return max(consec_counter, left, right)

        return dfs(root, float('-inf'), 0)
