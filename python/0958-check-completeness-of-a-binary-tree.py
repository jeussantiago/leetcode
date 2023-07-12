# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        Level Order Traversal
        (Queue)

        if we encounter a null in the queue, everything after the null should be null also

        Time: O(n)
        Space: O(n)
        '''
        isComplete = False
        q = collections.deque([root])
        while q:
            node = q.pop()

            if not node:
                isComplete = True
            else:
                if isComplete:
                    return False

                # add the nodes children
                q.appendleft(node.left)
                q.appendleft(node.right)

        return True
