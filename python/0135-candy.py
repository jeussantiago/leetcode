class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        [4,4,3,2,1,0,1,2,3,1,4]
        - 2 passes. one forward, and one backwards
        - if the current rating is bigger than the preevious rating then 
            - current candies for current kid = previous kid candies + 1
            - since we're coming from two side, one side might be bigger than the other
                - take the bigger number and +1 that

        Time: O(n)
        Space: O(n)
        '''

        N = len(ratings)
        if N == 1:
            return 1

        candies = [1 for _ in range(N)]

        def helper(ratings, candies):
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i-1]:
                    candies[i] = max(candies[i], candies[i-1] + 1)
            return candies

        candies = helper(ratings, candies)
        candies = helper(ratings[::-1], candies[::-1])[::-1]
        return sum(candies)
