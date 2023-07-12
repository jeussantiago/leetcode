class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''
        can calculate distance between 2 bombs like a triangle
        c^2 = a^2 + b^2
        c = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
        - this is the distance between one bomb and another

        - if the radius is <= to c, then the other bomb will be detonated

        Build an adjacency list from these bombs
            - if the other bomb is within the radius of the current bomb, place this bomb into the current bomb adj list

        the adj list to show neighbors or in this case, which bombs are reachable when current bomb explodes

        Time: O(n^3)
            ; (n^2) creating the adj list - each bomb is being compare with each other bomb
            ; (n^3) traversing the graph
            ;   (n) start with each bomb
            ;   (n^2) go through all of its neighbors, which is the number of edges (n^2 is the highest edge count b/c each 
                        bomb could reach each and every other bomb)
        Space: O(n^2)
            ; number of edges in adj list
        '''
        # build adj list
        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]

                # distance between bomb 1 and bomb 2
                dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if dist <= r1:
                    adj[i].append(j)
                if dist <= r2:
                    adj[j].append(i)

        # count the number of neighboring bombs

        def dfs(i):
            if i in visited:
                return 0

            visited.add(i)
            for neigh in adj[i]:
                dfs(neigh)

        res = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            res = max(res, len(visited))

        return res
