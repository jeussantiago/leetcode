class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        n is the maxChoosableInteger
        Time: O(2^n)
        Space: O(n)
            ; (n) recursion stack
        '''
        seen = {}

        def canWin(available_numbers, remainder):
            if available_numbers[-1] >= remainder:
                # whoever's turn it is, they win the total is over the desiredTotaL
                return True

            key = tuple(available_numbers)
            if key in seen:
                return seen[key]

            # go through the possible numbers available to choose from
            for i in range(len(available_numbers)):
                # remove the current number from the available numbers, decrement the desired total remainder
                if not canWin(available_numbers[:i] + available_numbers[i+1:], remainder - available_numbers[i]):
                    # to win, the other person had to lose
                    seen[key] = True
                    return True

            # getting here means the other player won, so you lost
            seen[key] = False
            return False

        # see if we can even play the game
        totalSum = (maxChoosableInteger+1) * maxChoosableInteger / 2
        # if total sum of all numbers(factorial) is < desiredTotal then we can't play the game
        if totalSum < desiredTotal:
            return False
        # if the total sum == desiredTotal, then player 1 wins if maxChoosableInteger is odd
        # maxChoosableInteger=3, [1,2,3] ; desiredTotal=6
        # maxChoosableInteger=4, [1,2,3,4] ; desiredTotal=10
        # the winner is the LAST person who chooses
        if totalSum == desiredTotal:
            return maxChoosableInteger % 2

        # create the range of numbers that are available to choose from
        available_numbers = list(range(1, maxChoosableInteger + 1))
        return canWin(available_numbers, desiredTotal)
