# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Time: O(n)
            ; have to search all nodes - worst case is that its not there
        Space: O(logn)
            ; recursion stack
        '''

        if not root:
            return None

        if root.val == val:
            return root

        left = self.searchBST(root.left, val)
        if left:
            return left

        return self.searchBST(root.right, val)
