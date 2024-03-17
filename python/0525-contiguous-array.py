class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        hash map
        - key: running total
        - val: index where first found the running total

        - if running total found previously, we can use that as the reference point to 
        indicate that it is the missing value to make the subarray contiguous

        [0, 1, 0, 0, 1]
        -1, 0,-1,-2,-1      

        - position 5 has a running total of -1, this means that there is an extra 0
            - but because -1 is already in the hashmap(we've seen it before), we know
            that at an earlier point, there was an extra 0, so if we remove that 0,
            i.e. start the subarray at the index after that point, we can create a 
            contiguous subarray where there are an equal amounts of 1s and 0s

        Time: O(n)
        Space: O(n)
        '''

        # running total of 0 is even before we count the other numbers
        seen = {0: -1}
        running_total = 0
        maxLen = 0
        for i, num in enumerate(nums):
            running_total += (1 if num == 1 else -1)

            if running_total in seen:
                maxLen = max(maxLen, i - seen[running_total])
            else:
                seen[running_total] = i

        return maxLen
