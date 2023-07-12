"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
                             10
                  5                         15
            3           7             13         17
        1       4   6       8       11  12     16  18

        1-3-4
        6-7-8





        - get left, get left_returned
        - move left pointer node, to the furthest right(biggest number) since currently its in the smalles number
            - set current_node.left = left
            - set left.right = current_node

        - get right, get right_returned
        - move to furthers left(smallest number)
            - set current.right = right
            - right.left = current


        '''
        if not root:
            return root

        def helper(node):
            if not node:
                return

            left_branch = helper(node.left)
            if left_branch:
                # go to the biggest number
                while left_branch.right:
                    left_branch = left_branch.right

                node.left = left_branch
                left_branch.right = node

            right_branch = helper(node.right)
            if right_branch:
                # go to the smallest number
                while right_branch.left:
                    right_branch = right_branch.left

                node.right = right_branch
                right_branch.left = node

            return node

        node = helper(root)
        start, end = node, node
        # print(node.val)
        while start.left:
            start = start.left

        while end.right:
            end = end.right

        start.left = end
        end.right = start
        return start
