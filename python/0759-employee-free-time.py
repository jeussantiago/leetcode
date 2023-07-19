"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        '''
        Heap:

        [
            [[1,3],[4,6],[7,8]],
            [[2,4]],
            [[2,5],[9,12]]
        ]

        - throw the current indexes onto a minHeap along with the index in the array and the index in the employee
        [([1,3], 0, 0), ([2,4], 1, 0), ([2,5], 2, 0)]

        val = (start, end, schedule_ind, schedule[i]_ind)
        [([2,4], 1, 0), ([2,5], 2, 0), ([4,6], 0, 1)]
        start = 3

        - free_start represents the latest time someone is working
        - if free_start < the current work time start
            - this means that there is some free between the curretn time and the next starting time
            - we can record this
            [free_start, work_start]

            - now that we recorded the free time, update the value of the free start
            - we can update it to work_end since we know this person is not working during htat time
        - free_start >= current work start:
            - free_start is either in the range of the work hours, OR
              it is greater than the work end time
                - either way, we want the biggest possible value to set as the point where someone 
                is still working

        - remove first value since it will contain [-inf, work_start]

        n is the length of schedule array
        m in the length of employee array in schedule
        Time: O(nm * logn)
            ; (n * m) visit each node once
            ; (logn) push onto heap
            ; (logn) remove from heap

        Space: O(n)
            ; (n) heap
        '''
        minHeap = []
        for i, time in enumerate(schedule):
            heappush(minHeap, (time[0].start, time[0].end, i, 0))

        res = []
        free_start = float('-inf')
        while minHeap:
            # get next working time
            work_start, work_end, i, j = heappop(minHeap)
            # push next working time for employee
            if j < len(schedule[i]) - 1:
                item = schedule[i][j + 1]
                heappush(minHeap, (item.start, item.end, i, j + 1))

            # check if recorded time is in the range of the current employee's work time
            if free_start < work_start:
                res.append(Interval(free_start, work_start))
                free_start = work_end
            else:
                free_start = max(free_start, work_end)

        return res[1:]
