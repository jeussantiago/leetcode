# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        binary search
        Time: O(logn)
        Space: O(1)
        '''
        low, high = 1, n
        while low <= high:
            num = (low + high) // 2
            num_guess = guess(num)
            if num_guess == 0:
                return num
            elif num_guess == -1:
                high = num - 1
            else:
                low = num + 1
