# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        - preOrder traversal (want to get the node first)
        - pass as a parameter the level it is on

                3
            9           20
                    15      7

        root, 0 -> 3
        left(node.left, level+1); level=1 -> [3],[9]
        - go back to root since you can go forward
        right(node.right, level+1); ; level=1 -> [3], [9, 20] ; appeneded to current one


        Time: O(n) go through all nodes in bst
        Space: O(n) size of tree (n) and n the size of the list which contains all the values in bst
        '''

        def helper(node, level):
            if not node:
                return

            if len(res) <= level:
                res.append([])
            res[level].append(node.val)

            helper(node.left, level+1)
            helper(node.right, level+1)

        res = []
        if not root:
            return res

        helper(root, 0)
        return res
