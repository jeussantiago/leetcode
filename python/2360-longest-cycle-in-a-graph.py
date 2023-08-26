class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''
        [3,-1,4,2,3]
        {
            0: 1
            3: 2
            2: 3
            4: 4
        }

        [-1, 0, 4, 2, 3, 6, 7, -1]
        [-1, 0, 4, -1, 3, 6, 7, -1]
        [-1, 0, -1, -1, 3, 6, 7, -1]
        [-1, 0, -1, -1, -1, 6, 7, -1]
        [-1, -1, -1, -1, -1, 6, 7, -1]
        [-1, -1, -1, -1, -1, -1, 7, -1]
        [-1, -1, -1, -1, -1, -1, -1, -1]

        - set each number to -1 to show that it has been visited
        - record in a hashmap at what count the node was visited at
        - move on to next index

        - you visit 3 again, although 3 is set to -1 now, it also exist already in the set, which means that it s cycle
        - current count = 5, index 3 was encountered at count 2, => 5 - 3 is the length of the cycle

        - if the number is -1 and is not in the visited, then there is no cycle

        Time: O(n)
        Space: O(n)
        '''
        def getCycleLen(i):
            visited = {}
            cycle_count = 1
            while edges[i] != -1:
                visited[i] = cycle_count
                tmp = edges[i]
                edges[i] = -1
                cycle_count += 1
                i = tmp

            if i in visited:
                return cycle_count - visited[i]
            return -1

        longest_cycle_len = -1
        for i, num in enumerate(edges):
            if num != -1:
                cycle_len = getCycleLen(i)
                longest_cycle_len = max(longest_cycle_len, cycle_len)

        return longest_cycle_len
