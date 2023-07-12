class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        cache -> keep track of:
            - who's turn
            - ind in piles array
            - current M value

            -> value: amount of ALICE stones (we don't store bob's stones)
            - result will reflect this in that we dont add to bob's stones in the code

        Time: O(n^3)
            ; cache with looping
        Space: O(n^2)
            ; (2 * n * n)size is the size of the cache
                - 2 possibilities for isAlice
                - n for number of possibilities for i 
                - n for number of possibiles for M

        '''

        cache = {}

        def dfs(isAlice, i, M):
            if i >= len(piles):
                return 0

            if (isAlice, i, M) in cache:
                return cache[(isAlice, i, M)]

            res = 0 if isAlice else float('inf')
            total_stones = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break

                total_stones += piles[i + X - 1]
                person_stones = dfs(not isAlice, i + X, max(X, M))
                if isAlice:
                    res = max(res, total_stones + person_stones)
                else:
                    # to maximize Alice's stones, we have to minimize Bob's stones
                    res = min(res, person_stones)

            cache[(isAlice, i, M)] = res
            return res

        return dfs(True, 0, 1)
