# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        '''
        - lots of repeat code, but should be literal faster since
        you don't check for level odd or even each time

        Time: O(n)
        Space: O(2^n - 1)
            ; most space used ofr last row of tree
        '''

        q = collections.deque([root])
        level = 0
        while q:

            if level % 2 == 0:
                # even level
                prev_node = float('-inf')
                for _ in range(len(q)):
                    node = q.pop()

                    if node.val % 2 == 0 or node.val <= prev_node:
                        return False

                    if node.left:
                        q.appendleft(node.left)

                    if node.right:
                        q.appendleft(node.right)

                    prev_node = node.val

            else:
                # odd level
                prev_node = float('inf')
                for _ in range(len(q)):
                    node = q.pop()

                    if node.val % 2 == 1 or node.val >= prev_node:
                        return False

                    if node.left:
                        q.appendleft(node.left)

                    if node.right:
                        q.appendleft(node.right)

                    prev_node = node.val

            level += 1

        return True
