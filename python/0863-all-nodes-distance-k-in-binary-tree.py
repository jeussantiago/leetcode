# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        - convert the tree into a un-directed graph
        - since all node values are unique, can start the BFS
        from the target node and work your way until you reach teh surrounding k nodes away

        Time: O(n)
            ; (n) one pass to convert to un-directed adj list
            ; (n) BFS search for surrounding k nodes away
        Space: O(n)
            ; (n) adj list
        '''

        # create un-directed adj list graph
        adj = collections.defaultdict(list)

        def dfs(node, parent):
            if not node:
                return

            # add neighbors to current node
            if parent:
                adj[node.val].append(parent.val)
            if node.left:
                adj[node.val].append(node.left.val)
            if node.right:
                adj[node.val].append(node.right.val)

            # traverse to next nodes
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # BFS - search for k nodes away
        q = collections.deque([target.val])
        visited = set()
        while k > 0:
            for _ in range(len(q)):
                num = q.pop()
                visited.add(num)
                for neigh in adj[num]:
                    if neigh not in visited:
                        q.appendleft(neigh)

            k -= 1

        return list(q)
