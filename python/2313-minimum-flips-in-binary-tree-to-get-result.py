# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        '''
        base case:
            - if leaf == 1: 
                - return 1, 0
            - if leaf == 0:
                - return 0, 1

        - at each position, return the number of swaps require to achieved the results
        - in the base case example of leaf == 1
            - the return value is: it takes 1 swap to turn 1 to 0, it takes 0 swaps to turn 1 to 1

        - explore left and right nodes
            - return value is the number of swaps to turn current value False, and number of swaps to turn current 
            value to True
            > left_false_swap_count, left_true_swap_count = dfs(node.left)
            - similar to right

        OR (2)
            - to get a False value: need both left and right to be false
                left_false + right_false
            - to get a True value: we need left or right to be true, so we can just check the min of the 2 sides
                min(left_true, right_true)

        AND (3)
            - to get False: need left or right to be false
                min(left_false, right_false)
            - to get True: need both to be True
                left_true + right_true
        XOR (4)
            - to get False: need same values
                min(left_false + right_false, left_true + right_true)
            - to get True: need different values
                min(left_false + right_true, left_true + right_false)
        NOT (5)
            - if node.left exist:
                - to get False: we get the value of True
                - to get True: we get the value of False
                - return the flipped (true value in false place, false value in true place)
                left_true, left_false
            elif node.right exist:
                - exact same concept
                right_true, right_false

        n is the number of nodes in the tree
        h is the height of the tree
        Time: O(n)
        Space: O(h)
            ; recursion stack
        '''

        def dfs(node):
            # base case
            if node.val == 0:  # False - leaf node
                return (0, 1)
            elif node.val == 1:  # True - leaf node
                return (1, 0)

            # explore next gets and get the count to turn the current value True or False from both children
            if node.left:
                left_false, left_true = dfs(node.left)
            if node.right:
                right_false, right_true = dfs(node.right)

            # calculate the count to turn the current val true or false depending on the operation
            if node.val == 2:  # OR
                return (
                    left_false + right_false,
                    min(left_true, right_true)
                )
            elif node.val == 3:  # AND
                return (
                    min(left_false, right_false),
                    left_true + right_true
                )
            elif node.val == 4:  # XOR
                return (
                    min(left_false + right_false, left_true + right_true),
                    min(left_false + right_true, left_true + right_false)
                )
            else:  # node.val == 5 (NOT)
                return (left_true, left_false) if node.left else (right_true, right_false)

        return dfs(root)[result]
