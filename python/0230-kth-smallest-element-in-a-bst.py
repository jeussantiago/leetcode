# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        - binary search tree
        (everything on the left side of the tree is smaller than the node
        everything on the right side of the tree is bigger than the node)

        recursion:
        - go left
        - go right
        - combine the left, current node, right

        return combined[k-1]
        Time: O(n)
        Space: O(n)
        '''
        res = []

        def helper(node):
            if not node:
                return []

            leftTree = helper(node.left)
            res.append(node.val)
            rightTree = helper(node.right)

        helper(root)
        return res[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        iterative: 
        - go all the way left
        (this will be your smallest number in the tree)
        - if you go to the right node after that, and traverse all the way left, then that will
        be the second smallest number

        - traverse left until the last left node
        - decrease k by 1
        - if k == 0
            - this node is the kth smallest integer
        - else
            - move to the right node

        Time: O(k)
        Space: O(k)
        '''

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right
