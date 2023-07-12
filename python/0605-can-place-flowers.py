class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # T: O(n)
        # S: O(1)
        N = len(flowerbed)
        for i in range(N):
            if flowerbed[i] == 1:
                continue

            if (i == 0 or flowerbed[i-1] == 0) and (i == N-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

        return n <= 0
