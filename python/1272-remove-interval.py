class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(1)
        '''
        res = []
        remove_start, remove_end = toBeRemoved
        for start, end in intervals:
            if end < remove_start or start > remove_end:
                # don't remove interval
                res.append([start, end])
            else:
                # removing something
                if start < remove_start:
                    # partially remove right side of interval
                    res.append([start, remove_start])

                if end > remove_end:
                    # partially remove left side of interval
                    res.append([remove_end, end])

        return res
