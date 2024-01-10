# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        '''
        - turn tree into unidirectional adj list
        - by doing that, we can start from the infected node
        - have a visited node to not backtrack 

        Time: O(n)
            ; (n) create adj list
            ; (n) find time for infected node
        Space: O(n)
            ; (n) adj list
        '''

        # turn tree into unidirectional adj list
        adj = collections.defaultdict(list)
        q = collections.deque([root])
        while q:
            node = q.pop()

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                q.appendleft(node.left)

            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                q.appendleft(node.right)

        # find time for all nodes to be infected
        time = 0
        visited = set([start])
        q = collections.deque([start])
        while q:
            for _ in range(len(q)):
                node = q.pop()
                for neigh in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.appendleft(neigh)

            time += 1

        return time - 1
