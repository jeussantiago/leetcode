# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        '''
        0, [float('inf'), float('-inf')] => 1, [7,7]

        - at anyu given node, its children should follow these rules
            - the left child's upper range should be < than parent node
            - the right child's lower range should be > than the parent node

            - if this condition is True, this means that it is a continuation of a sub tree
                - we can add the count of the nodes in the left and right tree, make sure to include the current node as well
                - we need to adjust the range
                    - since it is a proper bst, we can make the lower range the left_child lower range
                    - make the right child the upper range
                    - we have to combat the inf and -inf from the nodes so just take the min and max

            - if False, this means that the current node does not follow BST rules
            - we don't want to add the current node 
                - just get the current largest subtree count from the left or right side
            - we want to make sure that the parent nodes of this node don't take this into account
                - make the range something that won't ever return True for the question above
                ( current_node > right child upper range => float(inf))
                ( current_node < left child lower range => float(-inf))

        Time: O(n)
        Space: O(logn) for the most part, the recursion stack will hold content equal to the height of the tree
        '''

        def dfs(node):
            if not node:
                return 0, [float('inf'), float('-inf')]

            left_count, left_range = dfs(node.left)
            right_count, right_range = dfs(node.right)
            node_range = [node.val, node.val]

            if (
                node.val > left_range[1] and
                node.val < right_range[0]
            ):

                largest_subtree_count = left_count + right_count + 1
                node_range[0] = min(node_range[0], left_range[0])
                node_range[1] = max(node_range[1], right_range[1])
                return largest_subtree_count, node_range

            else:
                largest_subtree_count = max(left_count, right_count)
                node_range = [float('-inf'), float('inf')]
                return largest_subtree_count, node_range

        res, _ = dfs(root)
        return res
