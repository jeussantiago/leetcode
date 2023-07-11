class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        Similar to Ugly Number II
        - only want factors of the primes

        - have an index for each prime
        primes =  [2,7,13,19]
        prime_i = [0,0,0 ,0 ]

        - have a dp start at [1]
        dp = [1]

        - up until n
            - get the minimum of the multiplications of the primes at their respective index
            - get min => 2 * dp[0], 7 * dp[0], 13 * dp[0], 19 * dp[0], 
            - min = 2
            - add that to the dp

            - for any of the values, calculated, if == min(2), then increase it's index
            - in this case we increase index of 2

        how it should look like after first iteration
        primes =  [2,7,13,19]
        prime_i = [1,0,0 ,0 ]
        dp = [1,2]

        - now repeat for n times


        Time: O(n * k) where k is the len of primes arr
        Space: O(n + k)
        '''
        N = len(primes)
        primes_ind = [0] * N

        super_ugly_num = [1]
        for _ in range(n-1):

            vals = []
            for i, num in enumerate(primes):
                vals.append(num * super_ugly_num[primes_ind[i]])
            min_val = min(vals)
            super_ugly_num.append(min_val)

            for i, val in enumerate(vals):
                if val == min_val:
                    primes_ind[i] += 1

        return super_ugly_num[-1]
