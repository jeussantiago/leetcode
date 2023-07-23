# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        '''
        - each node going to each branch, subtract 2 each time
        - if there are 0 nodes left to be added
            - just return the current node

        - return a list of the current node possibilities + just the node itself

        n is the number of nodes
        Time: O(2^(n/2))
            ; 2 decisions each time
            ; height of tree can be at most n/2 since each node needs to get both a left and right node
        Space: O(2^(n/2))
            ; cache size
        '''

        @lru_cache(maxsize=None)
        def dfs(n):
            # even number n would result in a non full binary tree where atleast 1 node has 1 child
            if n % 2 == 0:
                return []

            if n == 1:
                return [TreeNode()]

            res = []
            for i in range(1, n, 2):
                left = dfs(i)
                right = dfs(n - i - 1)

                # get every possibility of trees
                for l in left:
                    for r in right:
                        node = TreeNode(0, l, r)
                        res.append(node)

            return res

        return dfs(n)
