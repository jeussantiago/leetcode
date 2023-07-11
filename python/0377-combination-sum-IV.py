class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        - add the current ind
        - go to next ind
        - start again from ind 0

        - just start from beginning if there is remaining val in target
        - can keep a cache key=remaining and target=num_of_combinations
            - so if we revisit a remaing value, we can just check how many combinations create the ramining value

        T for target
        N for length of nums
        Time: O(T * N) 
                    ; the size of the cache is going to be filled with the number of combinataions at each T
                    ;   the number of combinations in nums
        Space: O(T)
                    ; (T) size of the cache
                    ; (T) recursion
        '''
        cache = collections.defaultdict(int)

        def dfs(remain):
            if remain == 0:
                return 1

            if remain in cache:
                return cache[remain]

            for num in nums:
                if remain - num >= 0:
                    cache[remain] += dfs(remain - num)

            return cache[remain]

        return dfs(target)
