# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''

        Time: O(n)
        Space: O(2*n)
        '''

        def helper(node, path):
            if not node:
                return

            # no children - leaf node
            if not node.left and not node.right:
                path += [node.val]
                # check the sum
                if sum(path) == targetSum:
                    res.append(path)
                return
            # 1 kid
            if not node.left:
                return helper(node.right, path + [node.val])

            if not node.right:
                return helper(node.left, path + [node.val])

            # 2 kids
            helper(node.left, path + [node.val])
            helper(node.right, path + [node.val])
            return

        res = []
        helper(root, [])
        return res
