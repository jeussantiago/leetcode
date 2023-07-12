class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Time: O(2n)
        #     : O(n)
        # Space: O(n) ; res

        highest_candy_kid = max(candies)
        res = [candy + extraCandies >= highest_candy_kid for candy in candies]
        return res
