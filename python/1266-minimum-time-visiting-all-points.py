class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        res = 0
        for i in range(1, len(points)):
            x_diff, y_diff = abs(
                points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1])
            diag_dist = min(x_diff, y_diff)  # diagonal movement
            # remaining horizontal or vertical distance
            remain_dist = max(x_diff, y_diff) - diag_dist

            res += diag_dist + remain_dist

        return res
