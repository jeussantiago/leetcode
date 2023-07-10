# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        - any traversal would work, will just do preorder traversal
        - if the current node is none, normally, we would just ignore that, but this
        time it will be usful for comparison to compare structure

        - keep the current value of the p tree and q tree wherever in the tree it is, None leaf nodes are part of the structure

        Time: O(maxSize(p, q))
        Space: O(1) not using extra space other than the trees that are already created
        '''

        def helper(nodeP, nodeQ):
            nodQ_val = nodeQ.val if nodeQ else None
            nodeP_val = nodeP.val if nodeP else None

            if nodeP_val != nodQ_val:
                return False

            if not nodeP:
                return True

            return (
                helper(nodeP.left, nodeQ.left) and
                helper(nodeP.right, nodeQ.right)
            )

        return helper(p, q)
