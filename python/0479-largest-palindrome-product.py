class Solution:
    def largestPalindrome(self, n: int) -> int:
        '''
        - depending on n, we can find the max and min numbers possible
        max = (10 ** n) - 1
        min = 10 ** (n - 1)

        if n = 2
            => max = (10 ** 2) - 1 = 100 - 1 = 99
            => min = 10 ** (2 - 1) = 10 ** 1 = 10

        - since wee want the biggest, we can work backwards, starting from 99 in this case
        - with the current number, we can create a palindrome by adding and reversing it like strings
            => "98" + "89" => "9889"
            => "90" + "09" => "9009"

        - to find the pair of numbers that make up the palindrome, we need to check if some number is evenly divisible with the palindrome
            - once again we can work backwards from the max number but our min number this time is the sqrt(palindrome)
            - sqrt(palindrome) is our min because one of the pairs of numbers has to be bigger than sqrt(palindrome) and the other has to be smaller
            - so the loop is looking for the bigger, then we can check for the smaller

            - now we just need to check if the bigger number is divisible into the palindrome and if the remaining (smaller second number) is <= the max number
            - we can now return the mod 1337

        Time: O()
            ; (10**n - 10**(n-1)) outer loop
            ; (10*n - sqrt(n*2)) inner loop
        Space: O(1)
        '''

        if n == 1:
            return 9

        max_num = (10 ** n) - 1
        min_num = 10 ** (n - 1)

        for i in range(int(max_num), int(min_num) - 1, -1):
            palindrome = int(str(i) + str(i)[::-1])
            for num in range(max_num, int(palindrome ** 0.5) - 1, -1):
                if palindrome % num == 0 and palindrome // num <= max_num:
                    return palindrome % 1337
