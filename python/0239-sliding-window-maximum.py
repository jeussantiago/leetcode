class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Monotonically Decreasing Queue:

        Increasing
        [1,1,2,3] k = 3
        - [1,1,2]
        - go back and compare to the highest number
        - 1 is < 2
        res = 2
        - 3 is > 2
        - pop 2, add 3
        res = 3

        Decreasing
        [8,7,6,9] k = 2
        - left most value in our deck is the value we add to the res
        - left most is the highest value
        [8,7], add 8
        [7,6], add 7
        [6,9], pop 6, add 9

        -------------------

        - if the values are decreasing, add to front of queue
        - if the values are increasing, remove the front of queue until they are decreasing no more
        - in this way, the biggest values are always at the leftmost
        [4,3,-3,-1,-5,5,6] k = 3
        [5,6]
        [5]
        - we save the index in the queue so we can keep track of the window size

        Time: O(n)
        Space: O(n)
        '''

        res = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # get rid of the left value if the window is too big
            if l > q[0]:
                q.popleft()

            # advance pointers and add biggest number to results
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
