class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
        sort the list

        adding to the results:
        target = 7
        [1, 2, 3, 5, 8]
         ↑        ↑
        left    right

        - if this combination works, then every combinatinon before the right pointer will also work
        [ (1,5), (1,3), (1,2) ]
        - we don't neeed to manually see them to know
        - we can just take the difference between the two indexes


        Time: O(nlogn + n^2) sorting + lookup
            : O(n^2)
        Space: O(1)
        '''

        res = 0
        nums.sort()

        def twoSumSmaller(start, total):
            smaller_than_target_count = 0
            l, r = start, len(nums)-1
            while l < r:
                totalSum = total + nums[l] + nums[r]
                if totalSum < target:
                    smaller_than_target_count += (r - l)
                    l += 1
                else:
                    r -= 1
            return smaller_than_target_count

        res = 0
        for i in range(len(nums) - 2):
            res += twoSumSmaller(i + 1, nums[i])

        return res
