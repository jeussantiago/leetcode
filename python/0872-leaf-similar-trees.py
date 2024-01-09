# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        Time: O(n + m)
        Space: O(logn + logm)
            ; recursion stack of going through both trees
        '''

        def getLeaves(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            return getLeaves(node.left) + getLeaves(node.right)

        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)

        return leaves1 == leaves2


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        Option 2

        - check the leaves on leaves2 with leaves1 so that you don't do the final pass
        '''

        def getLeaves(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            return getLeaves(node.left) + getLeaves(node.right)

        def checkLeaves(node):
            if not node:
                return True

            if not node.left and not node.right:
                print(node.val)
                if leaves1 and leaves1[0] == node.val:
                    leaves1.popleft()
                    return True

                return False

            return checkLeaves(node.left) and checkLeaves(node.right)

        leaves1 = collections.deque(getLeaves(root1))
        if not checkLeaves(root2):
            return False
        # if theres still items in leaves1, then its not valid
        if leaves1:
            return False

        return True
