class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        - if h < len(piles): unable to eat all the bananas

        - you can go it i, if i has < k, then you eat all the bananas, if it has more, you stay at i until all
        the bananas are gone
        - max k can be is max(piles)

        l, r = 1, max(piles) => 11

        mid = 6

        - run through the program to see the amount of hours it would take to complete
        with using (mid/6) bananas an hour

        - if koko can finish all the bananas in k times, she can also finish the bananas in k+1, k+2... times
        - this means that mincreasing the bananas/hour, its fine to include the current bananas/hour
        - if k <= h
            - reduce the bananas/hr
            - r = mid

        - koko can't finish all the bananas in k times, this means that we need to ignore this current bananas/hr
        - if k > h:
            - increase the bananas/hr
            l = mid + 1

        16, 30, 23
        16, 23, 19
        20, 23, 21
        22, 23, 22
        23, 23, 23

        - right is part of the solution, which means that it will be the minimum at the end
        - return right


        Time: O(nlog(m)) where n is length of the arr and m is the max of the arr
        Space: O(1)
        '''

        l, r = 1, max(piles)

        while l < r:
            # bananas/hr
            mid = (l + r) // 2

            # get amount of hours it takes to finish all the bananas
            hours = sum(math.ceil(pile/mid) for pile in piles)

            if hours <= h:
                r = mid
            else:
                l = mid + 1

        return r
