class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        # precision issues at big numbers 
        - could be 4.999999 or 5.000001
        '''
        # if n <= 0: return False
        # x = math.log(n) / math.log(3)
        # return x % 1 == 0

        '''
        simple loop solution
        '''
        if n > 0:
            while n % 3 == 0:
                n //= 3
        return n == 1
