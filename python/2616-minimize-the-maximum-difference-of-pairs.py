class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        '''
        sort
        [3,7,10,12,13] ; p = 2
           4, 3, 2, 1

        - the number of combinations changes depending on what the max difference is

        if max difference was 5
            combinations: [(7,10)=3, (12,13)=1]
            - valid since len=p
        if max difference was 4
            combinations: [(10,12)=2]
            - not valid since len!=p

        - binary search to narrow down the optimal max difference threshold
            if valid
                - this means, at this maxDiff(mid), we can find p pairs from nums from every maxThreshold also > mid
                right = mid - 1
                - we also set the results to the current maxDiff(mid)
            else
                - this means, at this maxDiff(mid), we can't find p pairs from nums if maxThresshold < mid
                left = mid + 1

        - max threshold could possibly be 10**9 but realistically its max(nums) - min(nums)

        n is the length of nums
        V is the max difference of nums (max(nums) - min(nums))
        Time: O(nlogV)
            ; (nlogn) sorting
            ; (n) greedy on nums to find if there is a valid set of pairs
            ; (logV) binary search
        Space: O(1)
            ; (n) sorting
            (but we don't really add that into the equation)
        '''
        def isValidMaxDifference(maxDiff):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= maxDiff:
                    i += 2
                    cnt += 1
                else:
                    i += 1

                if cnt == p:
                    return True

            return False

        if p == 0:
            return 0

        nums.sort()
        # min possible threshold, max possible threshold
        l, r = 0, nums[-1] - nums[0]
        max_diff = nums[-1] - nums[0]
        while l <= r:
            mid = l + (r - l) // 2
            if isValidMaxDifference(mid):
                max_diff = mid  # max difference
                r = mid - 1
            else:
                l = mid + 1

        return max_diff
