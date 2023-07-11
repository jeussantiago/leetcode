# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        '''
        - children can be the same value but uni-value subtrees can only count if they have
        the same value and is a child of the parent

        - go through the tree
        - roots are alwys going to be uni-value subtrees
        Deciding if we should include the parent into the count
        - if 2 children
            - check if left child, right child is equal to parent
        - if 1 child
            - check if the child == parent

        Time: O(n)
        Space: O(h)
        '''
        def helper(node):
            if not node:
                return (0, True)

            left = helper(node.left)
            right = helper(node.right)

            is_uni = True

            if node.left:
                is_uni = left[1] and is_uni and node.val == node.left.val
            if node.right:
                is_uni = right[1] and is_uni and node.val == node.right.val

            num_uni_subtrees = left[0] + right[0]
            if is_uni:
                return (num_uni_subtrees + 1, is_uni)
            return (num_uni_subtrees, is_uni)

        return helper(root)[0]
