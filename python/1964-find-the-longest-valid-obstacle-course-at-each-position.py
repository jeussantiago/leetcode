class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''

        N = len(obstacles)
        res = []
        dp = []
        for i, num in enumerate(obstacles):
            ind = bisect_right(dp, num)

            if ind == len(dp):
                dp.append(num)
            else:
                dp[ind] = num

            res.append(ind + 1)

        return res
