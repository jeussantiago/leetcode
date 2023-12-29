class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        Time: O(n * n * d)
            ; (n) job Difficulty list
            ; (d) number of days available
            ; (n) curr_difficulty
        Space: O(n * n * d)
        '''
        cache = {}

        def jobs(i, day, curr_difficulty):

            if (i, day, curr_difficulty) in cache:
                return cache[(i, day, curr_difficulty)]

            if i == len(jobDifficulty):
                if day == 0:
                    return curr_difficulty

                return float('inf')

            # add the job to the current day
            option_one = jobs(
                i + 1, day, max(curr_difficulty, jobDifficulty[i]))
            # start a new day with the current job - need to record the max_difficulty of the previous day
            option_two = float('inf')
            if day > 0:
                option_two = curr_difficulty + \
                    jobs(i + 1, day - 1, jobDifficulty[i])

            cache[(i, day, curr_difficulty)] = min(option_one, option_two)
            return cache[(i, day, curr_difficulty)]

        res = jobs(0, d, 0)
        return res if res != float('inf') else -1
