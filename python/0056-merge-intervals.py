class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        - doesn't completely state that the intervals[i] are increasing in order
        
        - sorting helps because we know the starting positions of each interval is going to be >= the next interval
        - the starting interval <= the previous ending interval
            (and existing interval is already in the array)
            - current ending interval is greater than the previous ending interval
            (if it wasn't, then we can just skip this interval b/c prev_start <= curr_start <= curr_end <= prev_end
            current is in between the previous star and end interals)
                - modify last inputed interval to keep the same start but update the current ending interval
                - update previous ending interval to current ending interval
        (add new interval, not everytime, only when the current start is greater than the previous end)
        - elif current start > previous end
            - add interval to list
            - update the previous start and end to the current start and end since there might be following intervals that
            will update the one we just added

        Constraints:
        - values >= 0

        Time: O(nlogn + n) ; sorting the list initially - running through the list one time
           => O(nlogn)
        Space: O(n) ; don't create space when sorting - results array

        '''
        # intervals = [[1,4],[2,3]]
        # intervals = [[1,4],[1,4]]
        # intervals = [[1,4],[0,2],[3,5]]
        # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for curr_start, curr_end in intervals:
            end = res[-1][1] #last ending position
            if curr_start <= end:
                res[-1][1] = max(end, curr_end) #update last ending position
            else:
                res.append([curr_start, curr_end])
        return res