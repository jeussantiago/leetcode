class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        - for each num
            - calculate the difference between variable difference and the number itself
                - this number reprsents the number you will be keeping an eye for in the following numbers
                to come in the array
                - if you have repeating numbers, carry over the bigger number

            - if the current number is in the cache, 
                - the current count does not start at 1 but instead starts at whatever it is in the dictionary + 1

        arr = [1,5,7,8,5,3,4,2,1], difference = -2
        {
            -1: 1
            3: 1
            5: 1
            6: 1
        }
        - 2nd 5 is now found in the cache
            - takes value of (1) + 1
            5 + (-2) = 3
            - update value of the next value youre looking for, whichever is the max
            {3: 1} => {3: 2}
        {
            -1: 1
            3: 2
            5: 1
            6: 1
        }
        - 3 is found in the array
        - next number looking for is 1: val= the present number + 1 = 2 + 1
        {
            -1: 1
            0: 2
            1: 3
            2: 1
            3: 2
            5: 1
            6: 1
        }
        - 1 found in array
        - update next number needed -> keep max of the two
        {
            -1: 4
            0: 2
            1: 3
            2: 1
            3: 2
            5: 1
            6: 1
        }

        - keep track of the longest sequence

        Time: O(n)
        Space: O(n)
        '''
        res = 1
        dp = {}
        for num in arr:
            subsequence_length = 1
            if num in dp:
                subsequence_length += dp[num]

            dp[num + difference] = subsequence_length
            res = max(res, subsequence_length)

        return res


'''
- go back on itself to check if teh values before are the difference away from the curreent number

Time: O(n^2)
Space: O(n)
'''
