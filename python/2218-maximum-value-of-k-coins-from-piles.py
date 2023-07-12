class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        '''
        choose:
            - to take the next item in the pile
            - or to go to the next pile

        memoization
            - key = (current_pile, how many coins still left)
            - val = coin total (save max) 

        s is the total number of coins in all piles
        n is the len of piles
        Time: O(k * s)
        Space: O(k * n)
        '''
        n = len(piles)

        cache = {}

        def dfs(curr_pile, coins_left):
            if curr_pile == n or coins_left == 0:
                return 0

            if (curr_pile, coins_left) in cache:
                return cache[(curr_pile, coins_left)]

            # skip current pile
            cache[(curr_pile, coins_left)] = dfs(curr_pile + 1, coins_left)
            total = 0
            # at most we can take up to however many coins are left, or if the amount of coins in the pile is less than that
            for j in range(min(len(piles[curr_pile]), coins_left)):
                total += piles[curr_pile][j]
                # go to the next pile
                cache[(curr_pile, coins_left)] = max(
                    cache[(curr_pile, coins_left)],
                    total + dfs(curr_pile + 1, coins_left - j - 1)
                )

            return cache[(curr_pile, coins_left)]

        return dfs(0, k)
