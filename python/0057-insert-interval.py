class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Solution 2:
        for through intervals
            - if start of newInteval is bigger than end of current interval
                - add the current interval to the result since we know it involve itself in where the enw interval goes or if it merges
            - the start of the new interal being between the current interval or the start of the current interval being
            between the new interval => doesn't matter since the start of the new interval is less than or equal to 
            the end of the current interval
                - min of the starts of both intervals
                - max of the ends of both intervals
                (save values as the newInterval)
                (don't add the new interval until we see that the start of the current interval is less than end of newINterval)
            - the end of newInterval is less than start of current interval
                (not including this interval anymore)
                - add the new interval to the results
                - add the rest of the non used intervals to the results

        Time: O(n) where n is the length of the interavls array - looks at each interval one time
        Space: O(n) results array
        
        '''
        # intervals = [[1,5]]
        # newInterval = [6,8]
        # intervals = [[1,5],[6,8]]
        # newInterval = [5,6]
        # intervals = [[1,2],[5,6],[7,8],[9,10]]
        # newInterval = [3,4]
        # intervals = [[3,5],[12,15]]
        # newInterval = [6,6]
        # print(intervals, "::::", newInterval)
        # print('---------------')
        res = []
        for i in range(len(intervals)):
            #stopping point is when end of newInterval is less than start of current interval
            if newInterval[1] < intervals[i][0]:
                #add the current interval
                res.append(newInterval)
                #add rest of unused intervals
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # start of new interval > end of current interval
                res.append(intervals[i])
            else:
                # update newInterval because we know that the current index merges with newInterval
                # don't add to results because we need to see if the following intervals need to merge
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res

        

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Solution 1:
        - non-overlapping
        - intervals is sorted ascending order by start at i

        Solution 1:
        go through intervals
            - check if the newInterval start is between the current interval start and end
            (or is the current interval star is between thenew interval end)
            - this determines what our start interval is
                - start = min(new_interval_start, curr_interval_start)
                - end = max(new_interval_end, curr_interval_end)
                - while index hasn't gone out of bounds and end > curr_interal_start:
                    end = max(end, curr_interval_end)
                - add interval to res
        
        Time: O(n) where n is the length of the interavls array - looks at each interval one time
        Space: O(n) results array
        '''
        # empty intervals
        if not intervals: return [newInterval]
        # new interval before current interals
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        # new interval after current intervals
        if intervals[-1][1] < newInterval[0]: return intervals + [newInterval]

        res = []
        i = 0
        while i < len(intervals):
            #checks if the interval is between the start and end of a current interval and vice versa
            if (
                intervals[i][0] <= newInterval[0] <= intervals[i][1]
                or newInterval[0] <= intervals[i][0] <= newInterval[1]
                ):
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                # checks next intervals to see if it is still part of the merge (start of current interval <= end interval of merge)
                i += 1
                while i < len(intervals) and intervals[i][0] <= end:
                    end = max(end, intervals[i][1])
                    i += 1
                # reached the point where the new interval doesn't belong in the merged interval
                res.append([start, end])
                #add the rest of the intervals that weren't used
                res.extend(intervals[i:])
                break

            # add the current interval since it doesn't meet any requirements
            res.append(intervals[i])

            #check if the newInterval belongs in between intervals (end of current and start of next)
            if i < len(intervals)-1 and newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
                res.append(newInterval)
                #attach rest of interval
                res.extend(intervals[i+1:])
                break

            i += 1

        return res

