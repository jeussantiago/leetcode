# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        keep track of the left and right side of the root
        - treat each side like its own tree
        - does each treet look excatly like each other when you flip them?
        - when you traverse:
            - traverse left tree to left child while right tree to right child
            - traverse left tree to right child  while right tree to left child

        Time: O(1/2 n)
        Space: O(n)
        '''

        def isSameTree(leftTreeNode, rightTreeNode):
            # Null child
            if not leftTreeNode or not rightTreeNode:
                return leftTreeNode == rightTreeNode

            # different tree structure/values
            if leftTreeNode.val != rightTreeNode.val:
                return False

            return (
                isSameTree(leftTreeNode.left, rightTreeNode.right) and
                isSameTree(leftTreeNode.right, rightTreeNode.left)
            )

        return isSameTree(root.left, root.right)
