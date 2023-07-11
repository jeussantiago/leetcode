class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Solution 1:
        - 0 and 1 are not primes
        - Solution 1 (might be ok for interviews) - (but time limit exceeds):
        go through the range of [2,n] => num
            - for each number, go through the range [2, 2/n + 1] => i
                - check if the number is divisible
                (num % i) == 0 => not prime b/c the number is divisible by something other than itself

        Time: O(n^2)
        Space: O(1)

        Solution 2 (Sieve of Eratosthenes algorithm):
        - create an array of size n where each value is False
        - go through [2,n] (problem says not to include n)
        - go through all the multiples of a number until n
            (don't set the number itself to true, only the multiplications that are < number)
        Ex:
        n = 10
        [F,F,F,F,F,
         F,F,F,F,F]
        - go through [2,n]
        - i = 2
        [F,F,T,F,T,
         F,T,F,T,F]
        - if i is True: go to next number
        - if i is False
            - a prime number, increase some counter
            - calculate the multiples < n

        Time: O(n)
        Space: O(n)
        '''
        if n == 0 or n == 1:
            return 0

        primes = [False] * n
        primes[0] = True
        primes[1] = True
        output = 0
        for i in range(n):
            if not primes[i]:
                output += 1
                for multiple in range(i * i, n, i):
                    primes[multiple] = True

        return output
