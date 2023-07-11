class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time: O(nlogn)
        # Space: O(1)
        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key=lambda x: x[0])
        prev_end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            start_time, end_time = intervals[i][0], intervals[i][1]
            if start_time < prev_end_time:
                return False
            prev_end_time = end_time

        return True
