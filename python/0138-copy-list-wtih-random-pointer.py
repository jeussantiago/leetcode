"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Time: O(n)
        Space: O(n)
        '''
        if not head:
            return None

        clone = {}
        cur = head
        clone[cur] = Node(cur.val)

        while cur:
            if cur.next:
                if cur.next not in clone:
                    # create the next node
                    clone[cur.next] = Node(cur.next.val)
                clone[cur].next = clone[cur.next]

            if cur.random:
                if cur.random not in clone:
                    # create the random node
                    clone[cur.random] = Node(cur.random.val)
                clone[cur].random = clone[cur.random]

            cur = cur.next

        return clone[head]
