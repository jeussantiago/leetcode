# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        '''
        [1,2,3]
        - each node
        - remove the node from the array n and create a subtree with that
        1 - [2,3]


        '''
        def dfs(start, end, cache):
            if start > end:
                return [None]
            if (start, end) in cache:
                return cache[(start, end)]
            res = []
            for i in range(start, end+1):
                leftSubTree = dfs(start, i-1, cache)
                rightSubTree = dfs(i+1, end, cache)

                for left in leftSubTree:
                    for right in rightSubTree:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        res.append(node)
                        cache[(start, end)] += [node]

            return res or [None]

        cache = collections.defaultdict(list)
        output = dfs(1, n, cache)
        return output
