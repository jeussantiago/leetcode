class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        [0,20,20,20,40,90,90,90,150,150]

        [(2,40), (3, 40), (5, 60), (6, 110), (9, 170), (10, 170)]
        [(2, 1, 40), (3, 1, 20), (5, 2, 20), (6, 4, 70), (9, 6, 60), (10, 3, 100)]
        (end_time, start, time, profit)

        - bisect_right
            - if value == 0: just add number to stack or previous on stack
            - otherwise: can take that value + curr_payout
        - OR take previous(top of stack) value
        max(stack[-1].profit, bisect_right_ind.profit + curr_payout )

        - sort by end_time

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) going through all times
            ;   (logn) find the last start time and the maxProfit at that time
            ;   (1) calculate current profit for current day
        Space: O(n)
        '''
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort()
        dp = []
        for end, start, payout in jobs:
            # find the last job before the start of this job
            ind = bisect_right(dp, start, key=lambda x: x[0])
            # the profit befor the start of this job
            profit_before_start = 0 if ind == 0 else dp[ind-1][1]
            # the last job's profit (on top of stack)
            prev_day_profit = dp[-1][1] if dp else 0
            # current profit is going to be the last job's profit or the profit before
            # starting the current job + the current payout
            curr_profit = max(prev_day_profit, profit_before_start + payout)
            # add job to stack
            dp.append((end, curr_profit))

        return dp[-1][1]
