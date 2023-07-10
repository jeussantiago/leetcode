# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
                     3
             9               20
        1       2       15         7

        pre-order (nlr):
        [3,9,1,2,20,15,7]

        in-order (lnr):
        [1,9,2,3,15,20,7]

        - 3 is root in preorder
        - index of 3 in inorder is 3, everything left of 3 is the left substree and everything righ of 3 is the right subtree
        [1,9,2] [3] [15,20,7]
        - increase preorder iterator by 1
        - 9 is next, by using the left subtree, we can see the left and right subtreee
        [1] [9] [2]

        - continually create left and right subtrees
        - if the left index > right index, stop current cycle: return
        - b/c if the left > right: it means that we have reached the leaf node

        Time: O(n) we look through every value in preorder, but use inorder as a stopper
        Space: O(n) bst

        '''

        def helper(left, right):
            nonlocal preorder_ind
            if left > right:
                return None

            node_value = preorder[preorder_ind]
            node = TreeNode(node_value)

            preorder_ind += 1

            inorder_node_value_ind = inorder.index(node_value)
            node.left = helper(left, inorder_node_value_ind-1)
            node.right = helper(inorder_node_value_ind+1, right)

            return node

        preorder_ind = 0
        root = helper(0, len(preorder)-1)
        return root
