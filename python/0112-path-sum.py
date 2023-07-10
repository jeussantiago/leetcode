# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        - path has to go down to leaf
        if total sum > targetSum: 
            don't continue path
            return False

            1
        2

        - if theres 1 child, go down to that child
        - if theres 2 children, go down both kids
        - if theres no children, this means you have reached a leaf node - figure out operation

        Time: O(n)
        Space: O(1)
        '''

        def helper(node, nodeSum):
            if not node:
                return False
            nodeSum += node.val
            # no children - leaf node - does the sum of the nodes == target sum
            if not node.right and not node.left:
                return nodeSum == targetSum
            # one child
            if not node.right:
                return helper(node.left, nodeSum)
            if not node.left:
                return helper(node.right, nodeSum)
            # two children
            return (
                helper(node.left, nodeSum) or
                helper(node.right, nodeSum)
            )

        if not root:
            return False
        return helper(root, 0)
