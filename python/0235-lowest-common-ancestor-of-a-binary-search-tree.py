# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Binary Search Trees (not binary trees which don't necessarily have ot be in order)
        - everything left of the node is < node.val
        - everything right of the node is > node.val

        - if current node <= or == p.val or q.val, then we have hit the lowestcommonAncestor

        Time: O(h) where h is the height of the tree
        Space: O(1)
        '''

        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
