class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        x^n
        - if x=0 => 0
        - if n=0 => 1
        - if n<0 => 1/x^n

        Solution 1:
        2^4 => 2^1 * 2^1 * 2^1 * 2^1
        - we can just make recursion calls unttil n = 0 where it returns 1 

        Time: O(n)

        Solution 2:
        Divide and Conquer
        2^10 = 2^5 * 2^5 = 2^5 * 2^2 * 2^2 * 2^1

        Time: O(logn)

        Constraints:
        - n is an integer (no decimals)
        '''
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            # n=5 -> n=2 : x^2 * x^2 = x^4 < x^5
            res = helper(x * x, n // 2)
            #take care of the case of x being odd or even
            return res * x if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res

