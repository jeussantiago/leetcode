class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        '''
        - keep 2 DPs, one for each line stop
            - at each position i, calculate the min cost to reach 

            dp_regular[]
            dp_express[]

        Calculate dp_regular i
            if i != 0         (staying on regular, switching from express)
                dp_regular[i] = min(dp_regular[i - 1], dp_express[i - 1]) + regular[i]
            else
                = regular[i]

        Calculate dp_express i
            if i != 0
                                    (switching from regular to express, staying on express)
                dp_express[i] = min(dp_regular[i - 1] + expressCost, dp_express[i - 1]) + express[i]
            else
                # can't avoid the expressCost since you have to get to this station
                = express[i] + expressCost

        Resulting DP:
            res[i] = min(dp_regular[i], dp_express[i])

        regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8

        dp_regular = [1, 7, 16, 19]
        dp_express = [13, 11, 14, 24]
        res = [1, 7, 14, 19]

        Time: O(n)
        Space: O(n)
        '''
        n = len(regular)
        dp_regular = [0] * n
        dp_express = [0] * n
        res = [0] * n
        # fill in the initial values
        dp_regular[0] = regular[0]
        dp_express[0] = express[0] + expressCost
        res[0] = min(dp_regular[0], dp_express[0])

        for i in range(1, n):
            dp_regular[i] = min(dp_regular[i - 1],
                                dp_express[i - 1]) + regular[i]
            dp_express[i] = min(dp_regular[i - 1] + expressCost,
                                dp_express[i - 1]) + express[i]
            res[i] = min(dp_regular[i], dp_express[i])

        return res
