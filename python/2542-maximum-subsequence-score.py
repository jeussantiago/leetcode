class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        - all we really care about is maximizing the minimum value in nums2
        - we just need to ask, "What is the maximum value I can create with this min_value at pos in nums2?"

        - if we sort the nums by nums2, and nums1 since we need to keep it in pairs

        nums1 = [2,1,3,3,2], nums2 = [2,2,1,3,4], k = 3
        tuple=(nums2, nums1)
        [(2,2),(2,1),(1,3),(3,3),(4,2)]
        sorted=[(4,2),(3,3),(2,2),(2,1),(1,3)]

        Greedy:
        - since you need k elements when calculating, we can just start from index k-1
        - at these positions, the nums2, is the minimum number in the set of k elements
        - and since we want to maximize the value, we just need to get the biggest numbers from 0 to k-2 from the start of the tuple,
        and add the current position value
        - we don't know which values are the biggest, so at each position we can keep a minHeap to keep track of the biggest numbers
        pos2 = (3 + 3 + 2) * 2
        pos3 = (3 + 3 + 1) * 2
        pos4 = (3 + 3 + 2) * 1

        - we are doing a lot of repeated work since the k-2 values that are being added are all the same, so we can calculate that beforehand

        - save the max value while going through this

        Time: O(nlogn)
                ; (nlogn) sorting
                ; (nlogk) traversal/greedy
                ;   (logk) heappush/heappop
        Space: O(n) 
                ; (n) sorting
                ; (n) list of tuples
                ; (k) heap

        '''

        # sorted decreasing order
        nums = sorted(zip(nums2, nums1), key=lambda x: -x[0])

        res = 0
        nums1_sum, minHeap = 0, []
        for nums2_val, nums1_val in nums:
            heapq.heappush(minHeap, nums1_val)
            nums1_sum += nums1_val

            if len(minHeap) > k:
                nums1_pop = heapq.heappop(minHeap)
                nums1_sum -= nums1_pop

            if len(minHeap) == k:
                res = max(res, nums1_sum * nums2_val)

        return res
