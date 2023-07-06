class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1) array has to have atleast 3 integers
        2) numbers can be both negative and positive

        sliding window - move the pointers right or left depending if you are greater or lower than zero
        sort - makes life easier for sliding window
        add the first/current number to see if they add to zero
        if less than zero -> move the left pointer rightwards by 1
        if greater than zero -> move the right pointer leftwards by 1
        if zero -> add to array
        Time: O(nlogn) + O(n^2) - sorting + 1 loop to tell us the value and 1 loop to solve 2sum where n is the size of the array
        Time: reduces to O(n^2)
        Space: O(1) or O(n) because sorting takes up some memory in some libraries
        '''
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            #we don't want to reuse the same value i.e. [-3, -3, 0, 1, 2] - continue to next iteration of loop
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    threeSum = [num, nums[l], nums[r]]
                    if threeSum not in res:
                        res.append(threeSum)
                    l += 1
                    #we don't want to reuse the same value i.e. [-3, -3, 0, 0, 1, 1] 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

