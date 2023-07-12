class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        arr2 = [3,4,5]
        arr1 = [1,7,2,3]

        arr2 = [3,4,5]
        arr1 = [1,2,10,11,1]

        ** sort arr2

        DFS:

        - keep track of:
            - current arr1_ind (i)
            - the previous number
            (this value can change depending on if we decided to leave the number alone or change with arr2 value)

        if arr1[i] > prev_num
        (increasing)
            - leave it alone, and proceed to the next i index
            OR
            - change it with a value from arr2
            - value from arr2 is smallest number that is greater than the prev_num 
                - done with binary search
                - if there is no value > the prev_num, then we can just return float('inf') for this branch
            - add 1 to the count of steps

        if arr1[i] <= prev_num
        (decreasing)
            - can't leave alone
            - find the smallest value in arr2 > prev
            - add 1 step

        - save the minimum amount of steps in cache

        n is arr1 length
        m is arr2 length
        Time: O()
            ; (mlogm) arr2 sorting
            ; (n * m * logm)
            ; (n * m) time is dependent on the possible values in the cahce, there can be n number of (i) values
            and m + 1 number of (prev) values
                ; (logm) binary search on arr2
        Space: O(n * m) ; cache
        '''
        arr2.sort()

        N, M = len(arr1), len(arr2)
        cache = {}

        def dfs(i, prev):
            if i >= N:
                return 0

            if (i, prev) in cache:
                return cache[(i, prev)]

            cache[(i, prev)] = float('inf')
            if arr1[i] > prev:
                # leave alone
                cache[(i, prev)] = dfs(i + 1, arr1[i])

            j = bisect_right(arr2, prev)
            if j < M:
                # valid value in arr2
                steps = 1 + dfs(i + 1, arr2[j])
                cache[(i, prev)] = min(cache[(i, prev)], steps)

            return cache[(i, prev)]

        res = dfs(0, -1)

        return -1 if res == float('inf') else res
