class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        calculating square of digits
        method 1:
        - split the nums into str then turn them back to int to square them
        - then add the total

        method 2:
        - square the remainder (n % 10)**2
        - update the number by dividing by 10 (n = n // 10)

        n = 19
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1

        n = 2
        2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
        - 4 appears a second time, this means that itll be in an infinite loop

        Solution 1:
        - have a set to keep the repeated numbers
        - if the current number is in the set then there will be an infinite loop

        Time: O()
        Space: O(n)

        Solution 2 (Cycle linekd list) - (more space efficient):
        - similar to linked list cycle
        - have a slow and fast pointer
        - advance the slow pointer once and the fast pointer twice
        (pointers refer to squaring the digits)
        - when the numbers converge then your done

        - if the number is 1, then true, otherwise false

        Time: O()
        Space: O(1)
        '''
        slow, fast = n, self.sumDigitSquared(n)

        while slow != fast:
            slow = self.sumDigitSquared(slow)
            fast = self.sumDigitSquared(fast)
            fast = self.sumDigitSquared(fast)

        return slow == 1

    def sumDigitSquared(self, n):
        output = 0
        while n:
            output += ((n % 10)**2)
            n = n // 10

        return output
