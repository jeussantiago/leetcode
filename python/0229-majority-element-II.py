class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        - in Majority Element I, we find the magority element that appears N/2 times
        - the algorithm we use there is very at finding the element that appears the most amount of times
        (not the count of it however)

        - by constantly trying to use that same algorithm one after the other, then we can find out, in order,
        the most repeated elements
        - and element can only appear N/3 times in the array twice so we only need to keep track of 2 elements

        Time: O(n)
        Space: O(1)
        '''
        num1, count1 = None, 0
        num2, count2 = None, 0
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1 = n
                count1 = 1
            elif count2 == 0:
                num2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # we know which 2 elements appear the most - return the numbers if they appear more than N/3 times
        return [num for num in [num1, num2] if nums.count(num) > len(nums)/3]
