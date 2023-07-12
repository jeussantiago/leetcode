class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        [
            2,2,2,4,4,7,0
            0,0,0,0,0,0,0
            0,0,0,0,0,0,0
            0,0,0,0,0,0,0
        ]


        '''

        # this solution is more time efficient since it uses a cache
        dp = {}

        def dfs(curr_days_ind):
            if curr_days_ind >= len(days):
                return 0
            if curr_days_ind in dp:
                return dp[curr_days_ind]

            dp[curr_days_ind] = float('inf')
            for pass_len, pass_cost in zip([1, 7, 30], costs):
                j = curr_days_ind
                # go to the first day after the 1, 7, or 30  days pass has expired
                while j < len(days) and days[j] < days[curr_days_ind] + pass_len:
                    j += 1
                dp[curr_days_ind] = min(dp[curr_days_ind], dfs(j) + pass_cost)
            return dp[curr_days_ind]

        return dfs(0)
