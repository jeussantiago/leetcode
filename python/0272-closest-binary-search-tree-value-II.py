# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        '''
        [4,2,5,1,3], target = 3.714286, k = 2

        [(4,0.3), (2, 1.7)]

        Time: O(n + nlogn) go through the entyire tree + sort
            : O(nlogn)
        Space: O(n)
        '''

        res = []

        def helper(node):
            if not node:
                return
            res.append((node.val, abs(target - node.val)))

            helper(node.left)
            helper(node.right)

        helper(root)
        res = sorted(res, key=lambda tup: tup[1])
        return [tup[0] for tup in res[:k]]
        # if root.right and target <= root.val:
        #     helper(root.right)
        # if root.left and target >= root.val:
        #     helper(root.left)
