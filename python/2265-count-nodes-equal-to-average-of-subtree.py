# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        '''
        - post order traversal
            - go left and right first

        - if the node is NONE:
            - total=0 and num_nodes=0

        - add the total from left and right and the current node val
        - add the number of nodes left and right and the current node (+1)

        - calculate average = total // num_nodes
        - if average == node.val
            - add 1 to the total for the results

        Time: O(n)
        Space: O(1)
        '''
        def dfs(node):
            if not node:
                # total, num_nodes, res
                return (0, 0, 0)

            left_total, left_num_nodes, left_res = dfs(node.left)
            right_total, right_num_nodes, right_res = dfs(node.right)

            total = left_total + right_total + node.val
            num_nodes = left_num_nodes + right_num_nodes + 1
            res = left_res + right_res

            avg = total // num_nodes
            if node.val == avg:
                res += 1

            return (total, num_nodes, res)

        return dfs(root)[2]
