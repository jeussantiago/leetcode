# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        '''
                    1
            4               1
        1       1               5

        child = 4 , 5 
        grandchild =  2 , 0 

        (left grand + right grand + curr_ node) or
        (left child or left grandchild + right child or right grandchild)

        - if we rob the current node, we can't rob its children
            - can only rob grandchildren

        - if we don't rob the current node
            - we can rob it's children or any child of that


        - so if we rob, the parent can't touch this
        - if we don't rob, the parent can touch this node

        Time: O(n) visit each node once
        Space: O(n) recursion stack
        '''

        def dfs(node):
            if not node:
                # child, grandchild
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # choose to rob this node - we can only rob this node, if robbing from grandchild
            rob = node.val + left[1] + right[1]

            # choose to not rob this node - we can choose to rob from either the child or grandchild in left and right side
            not_rob = max(left) + max(right)

            # next node should not take the val of the current node since we robbed it - thats why we put it in the child position
            return (rob, not_rob)

        return max(dfs(root))
