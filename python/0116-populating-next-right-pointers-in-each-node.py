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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Queue:

        - get the length of the queue
        - for each item in queue in range current length of queue
            - get the left and right child, and put it at end of queue
                - if there are no children, don't add to end of queue
            - point node to next item in queue
            - if the node is the last node in the previous length of the queue, 
                - point node to null (don't need to do this step b/c it alreayd points to null)

        - this loop goes on until there nothing left in the stack



        Time: O(n) go through all nodes in binary tree   
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
                    queue.appendleft(node.right)

                if i < Q-1:
                    node.next = queue[-1]

        return root
