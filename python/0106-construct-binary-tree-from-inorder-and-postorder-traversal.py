# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
                    3
            9               20
        1       2       15      7

        inorder (lnr):
        [1,9,2,3,15,20,7]
        postorder (lrn):
        [1,2,9,15,7,20,3]

        - problem is similar to 105. Construct Binary Tree from Preorder and Inorder Traversal
            - exception is that postorder works backwards compared to preorder

        - check if left is > right: return None
        - create a ndoe with the postorder current index
        - index will start at length of postorder; works backwards
        - decrease postorder everythime you create a tree node
        - to get left and right for further recursion calls (sub trees/sub arrays); inorder.index(node_value)
        where node_value = postorder[postorder_current_index]

        - in the previous problem with inorder and preorder, we had to go node.left first then node.right second
        - in this problem, i think that order matters and that we have to go node.right first 

        Time: O(n) go through all values in postorder
        Space: O(n) not creating extra space like hash tables that some solutions use since im just using index, but creating bst os size n
        '''
        def helper(left, right):
            nonlocal postorder_ind
            if left > right:
                return

            node_value = postorder[postorder_ind]
            node = TreeNode(node_value)

            postorder_ind -= 1

            inorder_node_value_ind = inorder.index(node_value)
            node.right = helper(inorder_node_value_ind+1, right)
            node.left = helper(left, inorder_node_value_ind-1)

            return node

        postorder_ind = len(postorder)-1
        root = helper(0, len(postorder)-1)

        return root
