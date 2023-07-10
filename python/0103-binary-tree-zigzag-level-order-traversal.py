# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        - similar to 102. Binary Tree Level Order Traversal
        - have the level as a paremeter
        - create a new list if the level == len(result list)

        - if the level is an even number
            - append the values to the list normally at the end of the list
        - if the level is an odd number
            - add the values to the beginning of the list

                3
            9           20
                    15      7

        3 level:0 -> [[3]]
        9 level:1 -> [[3], [9]] (add 9 to beginning of list)
        20 level:1 -> [[3], [20, 9]] (add 20 to beginning of list)
        15 level:2 -> [[3], [20, 9], [15]] (add 15 to end of list)
        7 level:2 -> [[3], [20, 9], [15, 7]] (add 7 to end of list)

        Time: O(n) go through each node in bst
        Space: O(n) list the same size as bst
        '''

        def zigzagLevelOrder(node, level):
            if not node:
                return

            if len(res) == level:
                res.append([])

            if level % 2:
                # append to beginning of list
                res[level].insert(0, node.val)
            else:
                # append to end of list
                res[level].append(node.val)

            zigzagLevelOrder(node.left, level+1)
            zigzagLevelOrder(node.right, level+1)

        res = []
        if not root:
            return res

        zigzagLevelOrder(root, 0)
        return res
