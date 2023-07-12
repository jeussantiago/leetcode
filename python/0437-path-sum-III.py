# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        self.count = 0
        freq = collections.defaultdict(int)
        freq[0] = 1

        def dfs(node, prevSum):
            if not node:
                return

            currentSum = prevSum + node.val
            # the difference shows, if the number has appeared before, then we can ignore the node at that number and beyond
            # EX: target=3 ; 10 -> 8 -> 1 -> 2
            # when we get to the last node (2), what was seen before in terms of sums was 10, 18, 19, and now 21
            # if we take the difference between the currentSum and targetSum, if this number appears in the sum dictionary from before
            # this means that we can go to that node and remove everything before that, mimicking a scenario where the path
            # start after that node
            # in this case, 18 appears in the dictionary, and so we mimick removing node 10 and 8 and starting the count at node 1
            diff = currentSum - targetSum
            if diff in freq:
                self.count += freq[diff]

            freq[currentSum] += 1
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)

            # we are now done with this branch of the tree, so the sum doesn't matter here anymore and
            # we need to remove it
            freq[currentSum] -= 1

        dfs(root, 0)
        return self.count
