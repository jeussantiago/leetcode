"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        if not root:
            return []

        res = []
        q = collections.deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop()
                level.append(node.val)
                for child in node.children:
                    q.appendleft(child)

            res.append(level)

        return res
