# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        n is the number of nodes in the tree
        h is the height of the tree
        Time: O(n)
        Space: O(n)
            ; (h) recursion stack
        '''
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, found_both_left = dfs(node.left)
            right_node, found_both_right = dfs(node.right)

            nodes_found = found_both_left + found_both_right
            if node.val == p.val or node.val == q.val:
                return (node, nodes_found + 1)

            if left_node and right_node:
                return (node, nodes_found)

            if left_node:
                return (left_node, nodes_found)

            if right_node:
                return (right_node, nodes_found)

            return (None, 0)

        node, nodes_found = dfs(root)
        if nodes_found != 2:
            return None
        return node
