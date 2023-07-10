# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
                    2
                3
            4
        5
        leaf node: has no children

        Time: O(n)
        Space: O(1)
        '''

        def helper(node):
            if not node:
                return 0

            # return 1 if both left and right are 0, no children
            if not node.left and not node.right:
                return 1

            # if one side has a child and the other doesn't, return the height of the side with a child
            if not node.right:
                return helper(node.left) + 1

            if not node.left:
                return helper(node.right) + 1

            # has left child and right child
            return min(helper(node.left), helper(node.right)) + 1

        return helper(root)
