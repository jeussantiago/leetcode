class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        - amount of coins per level is (k(k + 1))//2 where k is the current height
        if the current row has more coins than n:
            - r = row - 1
        if the current row has less coins than n:
            - l = row + 1

        Time: O(logn)
        Space: O(1)
        '''

        l, r = 0, n
        while l <= r:
            row = (l + r) // 2
            total_coins = (row * (row + 1)) // 2
            if total_coins == n:
                return row
            elif total_coins > n:
                r = row - 1
            else:
                l = row + 1

        return r
