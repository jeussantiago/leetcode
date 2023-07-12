class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        Graph DFS:

        - create adjacency list for numbers up to n
        Example 2:
        {
            0: [1,2,3]
            1: [2,3]
            2: []
            3: []
            4: []
            5: []
        }


        - keep track of how many extra ethernet cables we have (in example 2, there are 2 extra wires)
        - keep track of many network islands we have (in example 2, there are 3 network islands)

        - visited set

        - traverse through every computer
        - if the computer has previously been visited
            - explore it's connections
            - b/c this computer hasn't been visited, this is a new network island
            (network_islands += 1)

        Exploring connenctions:
        - if current computer is in the visited set
            - this is an extra connection, which is an extra wire
            - increase extra ethernet cable count (extra_cable += 1)

        - add current computer to visited set

        - go through the neighboring computer of the current computer
            - visit neighboring computer

        Time: O(n + E) visit every node (n) and edge (E) in tree
        Space: O(n + E)
        '''

        # create adjacency list
        conn = collections.defaultdict(list)
        for comp1, comp2 in connections:
            conn[comp1].append(comp2)
            conn[comp2].append(comp1)

        visited = set()
        cycle = set()
        extra_cables = 0
        # explore conneciton island

        def dfs(comp):
            # print(comp, cycle)
            if comp in visited:
                if comp not in cycle:
                    nonlocal extra_cables
                    extra_cables += 1
                return

            visited.add(comp)
            cycle.add(comp)
            for neigh_comp in conn[comp]:
                dfs(neigh_comp)
            cycle.remove(comp)

        # explore connections
        network_islands = 0
        for comp in range(n):
            if comp not in visited:
                network_islands += 1
                dfs(comp)

        if extra_cables < network_islands - 1:
            return -1
        return network_islands - 1
