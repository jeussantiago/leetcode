class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        '''
        - create adjacency list from edges

        - iterate over query item
            - find the the from start to end using BFS
            - turn path into a set

            - BFS from target node
                - if you enter a node that is in the path (set), this node is your answer

        e is the number of edges
        n is the number of nodes
        q is the length of query array
        Time: O((q * (e + n)))
            ; (e + n) create adjacency list
            ; (q) iterate over query array
            ;   (e + n) find the path from start to end (could iterate over everything in tree)
            ;   (e + n) find the closest to target node (could iterate over everything in tree)
            ; => (q * (e + n + e + n)) => (q * (e + n))
        Space: O(e + n)
            ; (e + n) adjaceny list
        '''

        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def findClosestPath(start, end):
            visited = set([start])
            q = collections.deque([(start, [start])])
            while q:
                node, path = q.pop()

                if node == end:
                    return path

                for neigh in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.appendleft((neigh, [neigh] + path))

            return []

        def findClosestNodeToPath(target, path):
            visited = set([target])
            q = collections.deque([target])
            while q:
                node = q.pop()

                if node in path:
                    return node

                for neigh in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.appendleft(neigh)

            return 0

        res = []
        for start, end, target in query:
            path = set(findClosestPath(start, end))
            res.append(findClosestNodeToPath(target, path))

        return res
