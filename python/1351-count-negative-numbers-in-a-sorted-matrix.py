class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        Binary Search
        Time: O(mlogn)
        Space: O(1)
        '''
        res = 0
        n = len(grid[0])
        for row in grid:
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r)//2
                if row[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            res += (n - l)

        return res


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        since the cols are also sorted, that means if a position is negative, everything under it will also be negative
        - you don't need to re count those positions, you can assume with certainty that it is negative there
        - so all you need to do is check the left positions and move the pointer if those positions are negative with the same assumptions
        Time: O(m + n)
        Space: O(1)
        '''
        res = 0
        n = len(grid[0])
        col_neg_ind = n - 1
        for row in grid:
            while col_neg_ind >= 0 and row[col_neg_ind] < 0:
                col_neg_ind -= 1

            res += (n - col_neg_ind - 1)
            print(n - col_neg_ind - 1)
        return res
