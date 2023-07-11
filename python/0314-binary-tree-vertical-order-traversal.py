# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS - level order traversal

        - keep a record of the order
            - since we're doing level order traversal, it takes care of the nodes the come at a greater height issue
            - we will be adding items to the queue from left to right, this takes care of the left to right order issue

            - items in the left of the results will have come earlier in the tree in terms of height as well as row

        - we just need to keep track of the columns
            - when we add the items to the list, add it with column value
            - if traverse left, -1 from column value
            - if traverse right, +1 from column value

        - Ex 2:
        [(3,0), (9,-1), (8,1), (4,-2), (0,0), (1,0), (7,2)]

        - need to also keep track of the min_column and max_column
            - b/c we need to create the size of the final list
            - in the example above: min_column = -2 ; max_column = 2
            - size of final list = 5 = 2 - (-2) + 1

        final_list = [[], [], [], [], []]

        - add the contents of teh traversal to the final_list at the correct index
            - the current index - min_column
            (3,0) => 0 + min_column => 0 - (-2) => 2
            (9,-1) => -1 + min_column => -1 - (-2) => 1
        final_list = [[], [9], [3], [], []]

        Time: O(2n) where n is the number of nodes in the tree
            : O(n)
        Space: O(2n) traversal list and final_list
            : O(n)
        '''
        if not root:
            return []

        # BFS - level order traversal, while keeping track of current column
        level_order_nodes = []
        min_col, max_col = 0, 0

        q = collections.deque([(root, 0)])
        while q:
            node, col = q.pop()
            level_order_nodes.append((node.val, col))
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.appendleft((node.left, col-1))

            if node.right:
                q.appendleft((node.right, col+1))

        # order the final list at the correct index
        size = max_col - min_col + 1
        res = [[] for _ in range(size)]

        for val, col in level_order_nodes:
            # there are no negative indexes, we need to ofset the negative ones to fit within array contraints
            res[col - min_col].append(val)

        return res
