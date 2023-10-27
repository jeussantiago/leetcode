class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        '''
        Greedy

        Time: O(n)
        Space: O(1)
        '''
        total_poisoned_time = 0
        for i in range(len(timeSeries) - 1):
            secs_poisoned_curr_time = min(
                duration, timeSeries[i + 1] - timeSeries[i])
            total_poisoned_time += secs_poisoned_curr_time

        # account for last attack
        return total_poisoned_time + duration
