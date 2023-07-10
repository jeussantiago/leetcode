# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        - have each side (left and right side return the max depth that it reaches)
        - at the null leaf, return a 0, every parent needs to add 1 to the node
        - if both left and right end up being the same number at the end, then it is balanced, return true
        - return value could be a tuple (level, boolean isBalanced)
        - make sure that boolean is both true in previous subtrees before checking if the difference is <= 1

        height balanced: heights of root subtree don't differ by more than 1 depth

        Time: O(n)
        Space: O(1)
        '''
        '''
        TreeNode{val: 1, 
        left: TreeNode{val: 2, 
            left: TreeNode{val: 3, 
                left: TreeNode{val: 4, 
                    left: None, 
                    right: None}, 
                right: None}, 
            right: None}, 
        right: TreeNode{val: 2, 
            left: None, 
            right: TreeNode{val: 3, 
                left: None, 
                right: TreeNode{val: 4, 
                    left: None, 
                    right: None}}}}

                    1
            2                2
        3                       3
    4                               4            

        '''

        def helper(node):
            if not node:
                return (0, True)

            left = helper(node.left)
            right = helper(node.right)

            return (
                max(left[0], right[0]) + 1,
                left[1] and right[1] and abs(left[0] - right[0]) <= 1
            )

        return helper(root)[1]
