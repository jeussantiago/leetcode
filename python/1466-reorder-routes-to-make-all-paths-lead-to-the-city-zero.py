class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        BFS:

        - bi directional adjacency list accompanied with 1 or 0 depending on if the direction was flipped
        0 = not flipped direction
        1 = flipped direction
        [[0,1],[1,3],[2,3],[4,0],[4,5]]
        {
            0: [(1,0), (4,1)]
            1: [(0,1), (3,0)]
            2: [(3,0)]
            3: [(1,1), (2,1)]
            4: [(0,0), (5,0)]
            5: [(4,1)]
        }

        0 = node is moving away from 0 city
        1 = node is moving towards 0 city

        - if a city has a 0 (not flipped sign), we need to flip it to the other direction to go
        towards city 0
            - increase output counter

        Time: O(n + e) where n is nodes and e is the edges
        Space: O(n + e)
        '''
        path = collections.defaultdict(list)
        for city_a, city_b in connections:
            path[city_a].append((city_b, 0))  # original direction
            path[city_b].append((city_a, 1))  # flipped direction

        res = 0
        q = collections.deque([0])
        visited = set([0])

        while q:
            current_city = q.pop()
            for neigh_city, direc in path[current_city]:
                if neigh_city not in visited:
                    visited.add(neigh_city)
                    if not direc:
                        res += 1

                    q.appendleft(neigh_city)

        return res
