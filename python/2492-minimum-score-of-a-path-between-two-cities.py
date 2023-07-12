class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        '''
        DFS: (Stack/Recursion)

        Time: O(n + E) visited all the nodes and edges of the graph
        Space: O(n) for the recursion stack and the visited set

        '''
        # create the graph

        cities = collections.defaultdict(list)

        for city_a, city_b, distance in roads:
            cities[city_a].append((city_b, distance))
            cities[city_b].append((city_a, distance))

        # traverse the graph

        min_dist = [float('inf')]
        visited = set()

        def dfs(city):
            if city in visited:
                return

            visited.add(city)
            for neighbor_city, distance in cities[city]:
                min_dist[0] = min(min_dist[0], distance)
                dfs(neighbor_city)

        dfs(1)
        return min_dist[0]


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        '''
        BFS: (Queue)

        Time: O(n + E) visited all the nodes and edges of the graph
        Space: O(n) for the visited set
        '''

        # create the graph

        cities = collections.defaultdict(list)

        for city_a, city_b, distance in roads:
            cities[city_a].append((city_b, distance))
            cities[city_b].append((city_a, distance))

        # traverse the graph

        min_dist = float('inf')
        visited = set([1])
        q = collections.deque([1])

        while q:
            current_city = q.pop()
            for neighbor_city, distance in cities[current_city]:
                # we want to get the distance between 2 cities even if we've visited it before
                # we can visit a city through a different path at an earlier point in time
                min_dist = min(min_dist, distance)
                if neighbor_city in visited:
                    continue

                q.appendleft(neighbor_city)
                visited.add(neighbor_city)

        return min_dist
