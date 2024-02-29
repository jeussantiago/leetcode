# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        BFS - level order traverse

        Time: O(n)
        Space: O(2^n - 1)
            ; last row coudl potentiall have the most nodes
        '''

        leftmost_node = root.val
        q = collections.deque([root])
        while q:
            leftmost_node = q[-1].val
            for _ in range(len(q)):
                node = q.pop()

                if node.left:
                    q.appendleft(node.left)

                if node.right:
                    q.appendleft(node.right)

        return leftmost_node
