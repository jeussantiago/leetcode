class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        [3,6,1,9]

        - can think of it like when we see a new number, we want to update the minimum for the current array position in order from least to greatest
            - check the first number
            - then second number

        Time: O(n)
        Space: O(1)
        '''
        # N = len(nums)
        # if N < 3: return False

        arr = [float('inf'), float('inf'), float('inf')]

        for num in nums:
            if num <= arr[0]:
                arr[0] = num
            elif num <= arr[1]:
                arr[1] = num
            else:
                return True
        return False
