class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        '''
        - can go to any city where y != x
        (this means that you can't go back onto a city unless you visit another city first)
                       0     1     2     3     4
        names       ["ATL","PEK","LAX","DXB","HND"]

                      0    1    2    3
        targetPath  [ATL, DXB, HND, LAX]

        + 1                
        [ATL, DXB, ATL] -> 
            +1
            [ATL, DXB, ATL, LAX]
            - in this path, edits =  2
            - no go back to visit the other neighbor of ATL
            +1
            [ATL, DXB, ATL, DXB]
            - in this path, edits =  2
            - go back to visit next neighbor
        +1
        [ATL, DXB, PEK] -> 
            [ATL, DXB, PEK, DXB] +1 ; edit distance = 2
            [ATL, DXB, PEK, LAX] +0 ; edit distance = 1
            [ATL, DXB, PEK, HND] +1 ; edit distance = 2

        - need to also point to the direction of the min distance between names

        e is number of edges ; v is the number of vertices ; T for the length of targetPath
        Time: O(e + v * e * T) 
                  ; O(e + v) create adjacency list
                  ; O(e * T) dfs, go to every edge but we only need to explore however many targets are in the targetPath
            : O(e * T)

        Space: O(e + v + e * T)
                  ; O(e + v) adjacency list
                  ; O(e * T) cache, (current_name_ind, current_targetPath_ind)
             : O(e * T)
        '''

        adj = collections.defaultdict(set)
        for loc1, loc2 in roads:
            adj[loc1].add(loc2)
            adj[loc2].add(loc1)

        next_path = {}
        cache = {}

        def dfs(names_ind, targetPath_ind):
            if (names_ind, targetPath_ind) in cache:
                return cache[(names_ind, targetPath_ind)]

            # if the name and target name is the same, the edit distance doesn't increase
            editDist = 0 if names[names_ind] == targetPath[targetPath_ind] else 1

            if targetPath_ind == len(targetPath) - 1:
                return editDist

            minEditDist = float('inf')
            minEditDistNeigh = float('inf')
            for neigh in adj[names_ind]:
                neighEditDist = dfs(neigh, targetPath_ind + 1)
                if neighEditDist < minEditDist:
                    minEditDist = neighEditDist
                    minEditDistNeigh = neigh

            # minimum edit distance at the current name and target index
            editDist += minEditDist
            cache[(names_ind, targetPath_ind)] = editDist
            # next ideal neighbor that minimizies the edit distance
            next_path[(names_ind, targetPath_ind)] = minEditDistNeigh

            return cache[(names_ind, targetPath_ind)]

        minDist = float('inf')
        start = 0
        for i in range(len(names)):
            name_minDist = dfs(i, 0)
            if name_minDist < minDist:
                minDist = name_minDist
                start = i

        # create minimum edit distance path
        res = [start]
        targetPath_ind = 0
        while targetPath_ind < len(targetPath) - 1:
            start = next_path[(start, targetPath_ind)]
            res.append(start)
            targetPath_ind += 1

        return res
