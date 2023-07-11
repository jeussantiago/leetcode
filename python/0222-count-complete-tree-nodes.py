# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        - can split this into sub - problems
        - if the tree is balanced (leftHeight == rightHeight):
            - can use the formula (2**height)-1 to get the height at that node
        - if its unbalanced (leftHeight > rightHeight):
        (this problem makes it so that right Height can't be bigger than left Height)
            - solve the sub-problem
            - +1 for the current node
            - then traverse through the left and right nodes
            - (while in recursion -> the left node might be balanced and return the formula,
            while the right might be unbalanced and keep trying to solve the sub-problem
            - at some point,the unbalanced sides would be blanced if you go far enough, since it'll
            just be a single node)

                    1
            2               3
        4       5       6

        - 1 is unbalanced
        - 2 is balanced -> get number of nodes
        - 3 is unbalanced
        - 6 is balanced
        - right side is none so returns 0

        Time: O(logn * logn)
        Space: O(1)
        '''

        def getTreeHeightLeft(node):
            if not node:
                return 0
            return 1 + getTreeHeightLeft(node.left)

        def getTreeHeightRight(node):
            if not node:
                return 0
            return 1 + getTreeHeightRight(node.right)

        def helper(node):
            if not node:
                return 0

            leftHeight, rightHeight = getTreeHeightLeft(
                node), getTreeHeightRight(node)

            if leftHeight == rightHeight:
                # balanced tree
                return (2**leftHeight) - 1
            else:
                # unbalanced
                num_nodes_left = helper(node.left)
                num_nodes_right = helper(node.right)
                return 1 + num_nodes_left + num_nodes_right

        return helper(root)
