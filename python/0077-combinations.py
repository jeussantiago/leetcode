class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        - combination has to of length k
        - numbers in combination are in the range of 1,n
        [1,2,3,4]

        Time: O(k * n ^ k) n is the base number of decisions to be made in the decision tree and the height of the tree is (k) length
        Space: O(n * k)
        '''
        res = []

        def backtracking(n_start, combo):
            if len(combo) == k:
                res.append(combo.copy())
                return

            for num in range(n_start, n+1):
                combo.append(num)
                backtracking(num+1, combo)
                combo.pop()

        backtracking(1, [])
        return res
