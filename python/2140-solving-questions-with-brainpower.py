class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            points, steps = questions[i][0], questions[i][1]

            next_question = 0 if i + steps + 1 >= n else dp[i + steps + 1]
            dp[i] = max(dp[i+1], next_question + points)

        return dp[0]
