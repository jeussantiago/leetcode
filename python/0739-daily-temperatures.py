class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Monotonic Stack

        Time: O(n)
        Space: O(n)
        '''
        dp = [0] * len(temperatures)
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):

            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                dp[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return dp


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Min Heap

        Time: O(nlogn)
            ; (n) iterate through all elements in array
            ; (logn) add to heap
            ; (logn) pop from heap
        Space: O(n)
            ; (n) heap
            ; (n) dp
        '''

        # minHeap = []
        # dp = [0] * len(temperatures)

        # for i, curr_temp in enumerate(temperatures):
        #     # remove the temperatures from the min heap that are lower than
        #     # the current temprature
        #     while minHeap and curr_temp > minHeap[0][0]:
        #         previous_lower_temp, previous_lower_temp_ind = heapq.heappop(minHeap)
        #         days_after_temp_increase = i - previous_lower_temp_ind
        #         dp[previous_lower_temp_ind] = days_after_temp_increase
        #     # add the current temp and index to the min heap
        #     heapq.heappush(minHeap, (curr_temp, i))

        # # there might still be items left in the minHeap - However, we
        # # don't need to pop them since we initialized the dp with values of 0
        # return dp
