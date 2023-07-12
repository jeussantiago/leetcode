class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        '''
        - lookinng at the partitions
        - the score is the sum of the last element in the previous partition and the first element
        in the current partition
            - adjacent numbers

        weights = [1,2,3,4,5,6,7,8,9] ; k = 4

        => [3, 5, 7, 9, 11, 13, 15, 17]

        weights = [1,9,5,3,7,4,8,2,6] ; k = 4

        => [10, 14, 8, 10, 11, 12, 10, 8]
        => [8, 8, 10, 10, 10, 11, 12, 14]

        - AFTER SORTING: the max possible number that can be created is k-1 from the right
        - AFTER SORTING: the min possible number that can be created is k-1 from the left

        - subtract these two numbers to find the answer

        Time: O(nlogn)
            ; (n) create pair weights
            ; (nlogn) sort
            ; (k) taking the difference to find answer
            ; => (n + nlogn + k)
        Space: O(n)
            ; (n) python sorting
            ; (n) pair weights array
        '''
        n = len(weights)
        adj_weights = [0] * (n - 1)
        for i in range(n - 1):
            adj_weights[i] = weights[i] + weights[i + 1]

        adj_weights.sort()

        # get the max and min possible score
        min_score, max_score = 0, 0
        for i in range(k - 1):
            min_score += adj_weights[i]
            max_score += adj_weights[n - 2 - i]

        return max_score - min_score
