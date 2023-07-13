class Solution:
    def countOdds(self, low: int, high: int) -> int:
        '''
        number of odds increases depending if low or high is odd
        Time: O(1)
        Space: O(1)
        '''
        count = 0
        if low % 2:
            count += 1
        elif high % 2:
            count += 1
        count += (high - low) // 2
        return count
