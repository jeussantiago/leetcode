class Solution:
    def numWays(self, n: int, k: int) -> int:
        '''
        post = 1 ; k = 7
        [_]
        - there would be 7 choices for colors => k
        => k choices
        - this works for n = 1


        post = 2 ; k = 7
        [_, _]
        - same color => k (7)
        - different => 
            - first post has k choices
            - second post has k-1 choices
            => k * (k-1) => number of different color combinations

        - there would be 7 choices for colors 
        => same color comb + different color comb
        => k + (k * (k-1))
        => or k^2

        - this formula works for n = 2


        post = 5 ; k = 7
        [_, _, _, _, _]
        - post 3
            - (i-2) == (i-1) (same color post)
            - can be the same color if (i-2) != (i-1)
                => 1 choice for color since it has to be the same
                => if the post are the same, this means that there are 
                    num choices for n=2 * 1
                    => or k^2 * 1
                    => totalways(2) * 1
                    => totalways(2)
                    => totalways(n-1)
                - but we can only paint this post the same color if post (i-1) != (i-2)
                - color comb for (i-2) * next post, diff color * this post, same color are previous
                    => totalways(n-2) * (k-1) * 1

            - (i-2) != (i-1) (different color post)
            - can be different color if (i-2) post == color of (i-1)
                => (k - 1) choices for color
                => if the post are different, this means that there are 
                    num choices for n=2 * (k-1)
                    => or k^2 * (k-1)
                    => totalways(2) * (k-1)
                    => totalways(n-1) * (k-1)

            - number of different choices for post 3 is 
                - same + different color comb
                => [totalways(n-2) * (k-1) * 1] + [totalways(n-1) * (k-1)]
                => [totalways(n-2) * (k-1)] + [totalways(n-1) * (k-1)]
                => ([totalways(n-2) * 1] + [totalways(n-1) * 1]) * (k-1)
                => ([totalways(n-2)] + [totalways(n-1)]) * (k-1)


        - if n = 3, number of different color choices
            => ([totalways(n-2)] + [totalways(n-1)]) * (k-1)

        - same idea for post 4 and 5
        - final formula
            => ([totalways(n-2)] + [totalways(n-1)]) * (k-1)

        Time: O(n)
        Space: O(n)
        '''

        if n <= 2:
            return k ** n

        total_ways = [0] * (n+1)
        total_ways[1] = k
        total_ways[2] = k**2

        for i in range(3, n+1):
            total_ways[i] = (total_ways[i-2] + total_ways[i-1]) * (k-1)

        return total_ways[n]
