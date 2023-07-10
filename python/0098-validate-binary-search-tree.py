# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        - traverse the tree
        - if left node, compare parent if greater than
        - if right node, comparte parent if less than
        - we can keep track of the parent using parameters
        - and the condition always has to be true
            - the current node has to be greater than the lower parent
            - the current node has to be less than the greater parent

        - if you move left in the tree
            - udpate the biggest sized parent/right parent
        - if you move right in the tree
            - update the smallest sized parent/left parent

                5
            3           7
                    4       8

        - -inf < 5 < inf
        (move left, update right boundary/highest - cause the left node needs be < parent)
        - -inf < 3 < 5
        (go back to root)
        (move right, update left boundary/lowest - cause the right node needs to be > parent)
        - 5 < 7 < inf
        (move left, update right boundary)
        - 5 < 4 < 7
        (False)

        - in this way, youre always making sure, the current node is within the boundaries

        Time: O(n) have to go through all nodes of a tree
        Space: O(n) we keep the entire tree
        '''

        def isValid(node, leftBoundary=float("-inf"), rightBoundary=float("inf")):
            if not node:
                return True

            # check if current node is within bounds
            if not (leftBoundary < node.val < rightBoundary):
                return False

            return (
                # move left, update right Boundary
                isValid(node.left, leftBoundary, node.val) and
                # move right, update left Boundary
                isValid(node.right, node.val, rightBoundary)
            )

        return isValid(root)
