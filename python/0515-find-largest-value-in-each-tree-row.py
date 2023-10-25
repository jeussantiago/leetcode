# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        BFS:
        - this problem requires you to explore every position since you dont know what value each node could possibly have

        - just keep track of the current row in DFS or do BFS 

        n is all the nodes in the tree
        Time: O(n)
        Space: O(2 ^ (n-1))
            ; the most amount of items in the BFS is going to be the last row
            ; (DFS would optimize by having the most amount of space usage in a given time be the height of
            ; the tree which is logn)
        '''
        if not root:
            return []

        res = []
        q = collections.deque([root])
        while q:
            max_num_in_row = float('-inf')
            for _ in range(len(q)):
                node = q.pop()
                # record max for row
                max_num_in_row = max(max_num_in_row, node.val)
                # add items for next row
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            res.append(max_num_in_row)
        return res

        '''
        DFS

        - we don't know the height of the tree so we will have to dynamically add new values or update values
        depending on if a row was visited before

        Time: O(n)
        Sapce: O(logn)
            ; recursion stack is going to be at most the height of the tree
        '''
        # res = []
        # def dfs(node, row):
        #     if not node:
        #         return

        #     if len(res) == row:
        #         # new row
        #         res.append(node.val)
        #     else:
        #         # udpate current row max
        #         res[row] = max(res[row], node.val)

        #     dfs(node.left, row+1)
        #     dfs(node.right, row+1)

        # dfs(root, 0)
        # return res
