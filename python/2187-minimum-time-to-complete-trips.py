class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        Time: O(nlog(n))

        '''
        # returns True if the total amount of time to complete the inserted time takes is
        # over the total Trip time
        def checkStatus(givenTime):
            total_time = sum(givenTime // t for t in time)
            return total_time >= totalTrips

        l, r = 0, min(time) * totalTrips
        while l <= r:
            mid = (l + r) // 2
            if checkStatus(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
