class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        '''
        undirected graph = bidirectional graph

        [0,2,4,5]
        [0,1,2,3,4,5,6]

        i = 0 -> i + 1
        3 left -> len(4) - i
        n - len() - i => 7 - 4 - 0 = 3
                         7 - 4 - 1 = 2
                         7 - 4 - 2 = 1
                         7 - 4 - 3 = 0

        [1,6]
        7 - (i+1) - (len(2) - (i+1))
        7 - 1 - (2 - 1)

        len(2) * ([n - len(2)] 5 - len(2))

        Time: O(n + e)
        Space: O(n + e)
        '''

        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        cycle = set()

        def dfs(node):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    cycle.add(neigh)
                    dfs(neigh)

        # number of non repeating pairs
        def countCyclePairs():
            c = len(cycle)
            return c * (c - 1) // 2

        connected_pairs = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                cycle = set([node])
                dfs(node)

                connected_pairs += countCyclePairs()

        total_pairs = n * (n - 1) // 2
        return total_pairs - connected_pairs
