class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        '''
        dfs w/ binary search
        - sort by start time

        - at each position, decide to: attend event or skip event
            - if we attend the event, we can find the next set of events using binary search
                - any start date after the end date (this is fine since the arr is sorted)
            - if we don't attend the event, we can just go to the next event

        - to reduce time, we can have a cahce
        - in cache key=(current_ind, current_k) val=total_value

        n is the length of the events arr
        Time: O(n * k * logn)
            ; get every value in cache
            ; (logn) binary search to find next index position
        Space: O(n * k)
            ; (n * k) max number of cache values
            ; (n) recursion stack

        Possible Optimization:
            - precompute the binary search before entering the loops
            - as it stands, even at the same index, we are doing binary search over the same results
            - if we did it beforehand, we could do a look up would would operate faster
        '''
        events.sort()

        cache = {}

        def dfs(ind, k):
            if ind == len(events) or k == 0:
                return 0

            if (ind, k) in cache:
                return cache[(ind, k)]

            # skip event - go to next event
            skipped_event = dfs(ind + 1, k)

            # attend event - find the next array position where you can attend event
            next_available_event_ind = bisect_left(
                events, events[ind][1] + 1, key=lambda x: x[0])
            attended_event = dfs(next_available_event_ind,
                                 k - 1) + events[ind][2]

            cache[(ind, k)] = max(skipped_event, attended_event)
            return cache[(ind, k)]

        return dfs(0, k)
