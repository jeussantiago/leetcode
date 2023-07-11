# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        '''
        - if you find the child, go back up
        - if the target is a left child
            - the parent is the in-order successor
        - if the target is a right child
            - the parent of this node is the in-order successor
                5
            3   
                4   
            target = 4 => in-order successor = 5

        - keep moving the successor forward if the p.val is < node.val
        - continuously traverse the tree

        Time: O(h) where h is the height of the tree
            : O(N) actual time complexity because we might find a skewed tree
        Space: O(1)
        '''
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor
