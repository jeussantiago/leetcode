# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        - return the very right side of the binary tree

                    1
            2               3
        6       5       7       4

            1
        2
        expected: [1,2]

        - last node on the level, or the first going right, then left
        - hash table telling me if level has been visited

        [1,3,4]
        - node, right,

        Queue method:
        (would save space since no call stack)

        - have the root in the queue
        - go through whatever is in the queue (the range of the current len of the queue)
        - the very first one we pop (index 0) is the node we can see from the right side
        - everything else, including the first one, add the children to the queue

        Time: O(n)
        Space: O(logn)

        '''
        q = collections.deque([root])
        res = []

        while q:
            N = len(q)
            rightNode = None
            for i in range(N):
                node = q.pop()
                if node:
                    # udpate the node, last one is the last node that appears
                    rightNode = node

                    # add children to the queue
                    q.appendleft(node.left)
                    q.appendleft(node.right)

            if rightNode:
                res.append(rightNode.val)

        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursion method

        Time: O(n)
        Space: O(h), where h is the height of the tree
        '''

        visited = collections.defaultdict(bool)
        res = []

        def helper(node, level):
            if not node:
                return

            if not visited[level]:
                res.append(node.val)
                visited[level] = True

            helper(node.right, level + 1)
            helper(node.left, level + 1)

        helper(root, 0)

        return res
