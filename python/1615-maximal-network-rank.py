class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        '''
        - an idea is to keep track of the nodes with the 2 highest connections and just -1 if they are connected
        - issue: when there is a city(A) with 3 connections and two cities with 2 connections, one connected to the city A and the other not

        - So we have to check all the node(vertices) pairs

        - create adjancency list
        - pair each city with every other city
            - if they are connected: subtract -1 connection
                - can check if city 2 is in the adj list of city 1

        e is the number of edges
        V is the number of vertices(nodes)
        Time: O(e + V^2)
            ; (e + V) create adjacency list
            ; (V^2) find the highest network pair
            (e + V + V^2)
        Space: (e)
            ; adjacency list
        '''

        adj = collections.defaultdict(set)
        for city_a, city_b in roads:
            adj[city_a].add(city_b)
            adj[city_b].add(city_a)

        res = 0
        for city_a in range(n):
            for city_b in range(city_a + 1, n):
                pair_network_rank = len(adj[city_a]) + len(adj[city_b])
                if city_b in adj[city_a]:
                    pair_network_rank -= 1

                res = max(res, pair_network_rank)

        return res
