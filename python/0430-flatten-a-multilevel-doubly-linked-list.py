"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        stack:

        - if you find that the current node has a child
            - if there is a next node, put the next node onto the stack
            - move the current pointer to the child

        elif no next node:
            - pop from the stack
            - make the current pointer the popped item

        Time: O(n)
        Space: O(n)
        '''

        node = head
        stack = []
        while node or stack:
            if node.child:
                # save next node into the stack
                if node.next:
                    stack.append(node.next)

                node.next = node.child
                node.child.prev = node
                node.child = None

            elif not node.next and stack:
                parent = stack.pop()
                node.next = parent
                parent.prev = node

            node = node.next

        return head
