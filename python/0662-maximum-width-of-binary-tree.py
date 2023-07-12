# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        node order number/value is determine by:
            if left child:
                - 2 * node num
            if right child:
                - (2 * node num) + 1

                1
            2          3
        4       5           7 

        BFS
            - keep track of the min and max number in each level

            - after each level, keep record of the max width

        n is the size of the tree
        Time: O(n)
        Space: O(n)
        '''
        res = 1
        q = collections.deque([(root, 1)])
        while q:
            low_width, high_width = q[-1][1], q[0][1]

            # add the children of the existing nodes
            for _ in range(len(q)):
                node, num = q.pop()
                # high_width = num
                if node.left:
                    q.appendleft((node.left, num * 2))

                if node.right:
                    q.appendleft((node.right, (num * 2) + 1))

            # record the width of the current level
            res = max(res, high_width - low_width + 1)

        return res
