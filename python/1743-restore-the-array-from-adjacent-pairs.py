class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        '''
        adjacentPairs = [[4,-2],[1,4],[-3,1]]

        [4,1,-3] or [-3,1,4] is valid (reverse array is the same thing)

        {
            4: [1,-2]
            -2: [4]
            1: [4,-3]
            -3: [1]
        }

        visited = {4,-2,1,-3}

        [-3,1,4,-2]

        - create an adj list out of the adjacentPairs
        - we start our array with the first pair b/c we know these two numbers are going to be 
        next to each other in the list

        Queue:
        - we start with the first number, and we traverse the adjacency list to build out
        the left side of the final array 4 -> 1 -> 3
            - q.appendleft()
        - then we staart again from the last number(which was the 2nd number) to build out the 
        right side of the array
            - q.append()

        - keep track of the visited numbers so that you don't add the same number again

        Time: O(n)
            ; (n) build the adjacency list
            ; (n) build the final array - traversing left side of array and right side
            ; of array
        Space: O(n)
            ; (n) adj list
            ; (n) visited set
            ; (n) final array queue
        '''
        adj = collections.defaultdict(list)
        for a1, a2 in adjacentPairs:
            adj[a1].append(a2)
            adj[a2].append(a1)

        visited = set([adjacentPairs[0][0], adjacentPairs[0][1]])
        q = deque([adjacentPairs[0][0], adjacentPairs[0][1]])

        # build left side
        while True:
            currNum = q[0]
            for neigh in adj[currNum]:
                if neigh in visited:
                    continue

                q.appendleft(neigh)
                visited.add(neigh)

            if len(adj[currNum]) == 1:
                break

        # build right side
        currNum, prevNum = adjacentPairs[0][1], adjacentPairs[0][0]
        while True:
            currNum = q[-1]
            for neigh in adj[currNum]:
                if neigh in visited:
                    continue

                q.append(neigh)
                visited.add(neigh)

            if len(adj[currNum]) == 1:
                break

        return q
