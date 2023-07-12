class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
        intervals = [[1,4],[2,3],[3,4]]
        res = [-1,-1,-1]
        - starting intervls array
        begginning_arr = [1,2,3]
        - loop through intervals and see where the end interval is located in the array
            - bisect_right
            - loc == len(beginning_arr)
                - leave alone, res at position is -1
            - otherwise
                - grab the tracked index of its original position and insert at current position

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) creating begginning array
            ; (n) loop through arr
            ;       (logn) check where to insert
            ; => (nlogn + n + nlogn)
        Space: O(n)
            ; (n) sorting
            ; (n) beginning_arr and res arr
        '''
        n = len(intervals)
        intervals = [(start, end, i)
                     for i, (start, end) in enumerate(intervals)]
        intervals = sorted(intervals, key=lambda x: x[0])

        res = [-1] * n
        beginning = [start for start, _, _ in intervals]

        for _, end, original_ind in intervals:
            pos = bisect_left(beginning, end)
            if pos < n:
                res[original_ind] = intervals[pos][2]

        return res
