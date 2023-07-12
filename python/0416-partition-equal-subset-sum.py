class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        - equal value == sum(nums)/2
        - if sum(nums) is odd, then it is impossible to arrive an qual half: return False

        - at every position, we can decided to include the num in the sum to reach the equal value or not include it
        (essentially to skip it incase it belongs in the other array)

        Dfs:
            - cache: key=(curr_i, total) value=Bool

        m is the subset sum
        n is th elength of nusm
        Time: O(n * m)
        Space: O(m)
        '''
        # odd sum
        if sum(nums) % 2:
            return False

        dp = set([0])
        target = sum(nums) // 2
        for num in nums:
            next_dp = set()
            for n in dp:
                next_dp.add(n + num)
                next_dp.add(n)
            dp = next_dp

        return target in dp
