# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
                1
            2               3
        0           4              5
                6       7       8       9

        depth = 2
        [0,6,7,8,9],[2,4,5],[3],[1]

        Time: O(n)
        Space: O(n)
        '''
        self.res = []

        def dfs(node):
            if not node:
                return -1

            left_height = dfs(node.left) + 1
            right_height = dfs(node.right) + 1

            max_height = max(left_height, right_height)
            if max_height == len(self.res):
                self.res.append([])

            self.res[max_height].append(node.val)
            return max_height

        dfs(root)
        return self.res


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.res = []

        def dfs(node, node_height):
            if not node:
                return node_height - 1

            if node_height > len(self.res):
                self.res.append([])

            left_max_height = dfs(node.left, node_height + 1)
            right_max_height = dfs(node.right, node_height + 1)

            max_height = max(left_max_height, right_max_height)

            self.res[max_height - node_height].append(node.val)

            return max_height

        dfs(root, 1)
        return self.res
