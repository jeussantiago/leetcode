# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        p = 5 and q = 2

        - even if we find one of the two, if the other side of the tree returns None, then we can
        only conclude that the lowest common ancestor is that singular node

        Time: O(n)
        Space: O(n) # call stack
        '''

        def helper(node):
            if not node:
                return
            if node == q or node == p:
                return node

            foundLeft = helper(node.left)
            foundRight = helper(node.right)

            if foundLeft and foundRight:
                return node

            elif foundLeft:
                return foundLeft
            elif foundRight:
                return foundRight

            return None

        return helper(root)
