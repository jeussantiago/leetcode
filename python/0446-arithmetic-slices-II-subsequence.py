class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
            2 4 6 8 10
        [
            {2: 0, 4: 0, 6: 0, 8: 0},
            {2: 1, 4: 0, 6: 0},
            {4: 1, 2: 2},
            {6: 1, 4: 1, 2: 3},
            {8: 1, 6: 1, 4: 2, 2: 4}
        ]

        similar to having 2 pointers
            - a leading pointer
            - then a trailing pointer that start from 0 and goes up to the leading pointer, not including the leading pointer position

        - at each position, calculate the difference between the leading and the trailing
        - check if the difference is in the dictionary position of the trailing pointer
        EX: if the leading pointer is at pos=2, num=6 
            and the trailing pointer is at pos1, num=4

                - the diff = 2
                - we then check the trailing pointer pos, if there exist a key=2, 
                (since the key represents the difference, val represents the number of valid subsequencse)
                - key=2 does exist, with a value of 1, so we add 1 to that and save it into the leading positions dictionary

        - solution answer is to sum up the last positions values

        Time: O(n^2)
        Space: O(n^2)
        '''

        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n)]
        res = 0

        # leading pointer
        for i in range(n):
            # trailing pointer
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1

                # this is here to counteract that you need 3 variables rather than 2
                res += dp[j][diff]

        return res
