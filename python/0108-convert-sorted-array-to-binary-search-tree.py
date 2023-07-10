# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        [-10, -3, 0, 5, 9]
        [-10, -3, 0, 4, 5, 9]
        len = even
        mid = right + left // 2
        3 = 6 + 0 // 2
        mid3 = 4
        node.left = mid of left subtree
        node.riht = mid of the right subtree

        node.left = left:0 right:3-1=2
        left subtree in the array of
        [-10, -3, 0]
        create node with mid
        mid = 1 = 0 + 2 // 2
        node.left = 0-0

        - similar to binary search

        Time: O(n)
        Space: O(n)
        '''

        def binarySearchCreateTree(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # left side of tree
            node.left = binarySearchCreateTree(left, mid-1)
            # right side of tree
            node.right = binarySearchCreateTree(mid+1, right)

            return node

        root = binarySearchCreateTree(0, len(nums)-1)
        return root
