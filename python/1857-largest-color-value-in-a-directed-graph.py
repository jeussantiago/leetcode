class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        '''
        Time: O(n + e) go through all the nodes and edges in the graph once
        Space: O(n + e)
        '''
        adj = collections.defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)

        def dfs(node):
            if node in path:
                # cycle
                return float('inf')

            if node in visited:
                # cycle and visited are 2 different things. visited tells us that the node dict was already calculated
                return 0

            visited.add(node)
            path.add(node)
            for neigh in adj[node]:
                if dfs(neigh) == float('inf'):
                    # cycle
                    return float('inf')

                for color, count in color_count[neigh].items():
                    # node might have multiple neighbors, we don't really care about which path has which certain number of
                    # colors. all we care about is the the max number of each color given a path
                    color_count[node][color] = max(
                        color_count[node][color],
                        color_count[neigh][color]
                    )

            # add the current node color to the count
            # index tells us the current color of the node
            node_color = colors[node]
            color_count[node][node_color] += 1

            path.remove(node)
            return max(color_count[node].values())

        N, res = len(colors), 0
        visited, path = set(), set()
        color_count = [collections.defaultdict(int) for _ in range(N)]
        for node in range(N):
            res = max(res, dfs(node))

        return -1 if res == float('inf') else res
