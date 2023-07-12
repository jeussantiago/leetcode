class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy
        Time: O(nlogn)
        Space: O(n)
        '''
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: (x[1]))

        interval_cnt = 0
        last_interval = float('-inf')
        for start, end in intervals:
            if start >= last_interval:
                last_interval = end
                interval_cnt += 1

        return n - interval_cnt


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        - sort the numbers
        [[1,3],[2,5],[4,5],[6,7],[6,8],[7,8]]

        - at each position in the dp, save the number of non-overlapping intervals
        - at eqach position, iterate in reverse order
            - if current_pos_end < start:
                - non-overlapping
                - save tehcount of their non-overlapping intervals
                - save the max

        - at this point, we'll have the max and we can just add +1 and save to current index

        [[1,3],[2,5],[4,5],[6,7],[6,8],[7,8]]
        [1,1,2,3,3,4]

        - the last position has a 4 which means that there are 4 intervals that don't overlap which each other
        - answer = len(intervals) - dp[-1]


        Time: O(n^2)
            ; (nlogn) sorting
            ; (n^2) fo through the arr and reverse back to check the dp
        Space: O(n)
            ; (n) sorting
            ; (n) dp
        '''
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        dp = [float('-inf')] * n
        for i in range(len(intervals)):
            max_interval_cnt = 0
            for j in range(i-1, -1, -1):
                # j_end_interval <= i_start_interval
                if intervals[j][1] <= intervals[i][0]:
                    max_interval_cnt = max(max_interval_cnt, dp[j])

            dp[i] = max_interval_cnt + 1

        return n - dp[-1]
