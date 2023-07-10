"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        - get current length of queue

        - pop the end of queue
        - add the children of the node
        - point current node to next node in queue
        (if current node is the last item in previous queue)


        Time: O(n)
        Space: O(1)
        '''

        if not root:
            return None

        queue = collections.deque()
        queue.append(root)

        while queue:
            Q = len(queue)
            for i in range(Q):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

                if i < Q-1:
                    node.next = queue[-1]

        return root
