# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        Solution 1:
        - go through bst inorder traversal
        - save all the nodes in a list
        - order the list by node val
        - go through node list and set the values to the values in order list

        Solution 2:
        - everything to the right of a parent is greater, there is an issue if you go to the left 
        most number in the right side and it doesn't meet those requirements
        - do inorder traversal
        - in inorder traversal, the output values will always increase in order
        - this means that if you keep track of the previous number value and the current number value, you 
        can see which number is in the wrong position
        - if previousNodeVal >= currentNodeVal then something is wrong
        - the currenNodeVal should always be greater than the previous node val according to inorder traversal
        - when you find the issue, save the previous node
        - when you find the second issue, save the current node
        - the reason you save different nodes is b/c they can't be the same node, you can't swap repeating nodes



        Time: O(n) go through the entire bst
        Space: O(1) save only the current and previous nodes
        """
        # solution 2
        def helper(node):
            nonlocal firstNode
            nonlocal secondNode
            nonlocal prevNode

            if not node:
                return

            helper(node.left)
            # previous node should always be less than current node
            if not firstNode.val and prevNode.val >= node.val:
                firstNode = prevNode

            if firstNode.val and prevNode.val >= node.val:
                secondNode = node

            prevNode = node

            helper(node.right)

        firstNode = TreeNode(None)
        secondNode = TreeNode(None)
        prevNode = TreeNode(float("-inf"))

        helper(root)
        # swap the two numbers that are out of place
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
