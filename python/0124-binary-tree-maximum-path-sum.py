# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
                1
            2           3
                    4       5

        - whats the max value on the left? res=2
        - whats the max value in the right?
        - a 3 shows up with children
        - go to its children
        - if you could split, max value would be res=5
        - return the max value running from one child to the root of the tree
        - but you can also potentially have a bigger path with 4 -> 3 -> 5
        - so we update the result with that potentially but we return the values of the split path

        Time: O(n)
        Space: O()
        '''

        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # split to the children
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)
            # if the child tree is negative, remove it from the path and start the path at the current node
            leftTree = max(0, leftTree)
            rightTree = max(0, rightTree)

            # case of path starting from left to current to right tree like in example above
            res[0] = max(res[0], leftTree + node.val + rightTree)

            # return the higher value between the children to see which path the parent should choose
            return node.val + max(leftTree, rightTree)

        dfs(root)
        return res[0]
