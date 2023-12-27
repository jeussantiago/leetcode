class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        res = 0
        prev_color = None
        prev_time = float('-inf')
        for i in range(len(colors)):
            curr_color, curr_time = colors[i], neededTime[i]

            if prev_color != curr_color:
                prev_color, prev_time = curr_color, curr_time
            else:
                # consecutive color
                if prev_time < curr_time:
                    res += prev_time
                    prev_time = curr_time
                else:
                    res += curr_time

        return res
