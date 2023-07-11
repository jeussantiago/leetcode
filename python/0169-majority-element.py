class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Take advantage of the fact that the majority element has to appear more than n/2 times

        - keep track of the current highest number, keep track of the count of the highest number
        - if the count == 0
            - set the new result to be the current number
            - increase the count +1

        - if you see another number that is the same as the result
            - increase the count +1
        - if you see a number that isn't the same as the result
            - decrease the count -1


        - at the end, since the majority shows up more than  n/2 times in the array, then
        it will remain as the result with some number of count >0


        Time: O(n)
        Space: O(1)
        '''

        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)

        return res
