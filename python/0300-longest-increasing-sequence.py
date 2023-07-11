class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        dp = []
        for num in nums:
            ind = bisect_left(dp, num)
            if ind == len(dp):
                dp.append(num)
            else:
                dp[ind] = num

        return len(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        [10,9,2,5,3,7,101,18]


        - at each number, go traverse backwards to find the last index where the number is < current number
        - if that number is found, we can take the subsequence length and +1
        - if not found, put a 1
        - store the subsequence length for each index in a dp array

        [10,9,2,5,3,7,101,18]
        [1 ,1,1,1,1,1, 1 , 1]

        - from ind 0, go back until a found number that is less than itself
            - its none, so leave it alone
        - ind 1 is the same
        - ind 2 is the same
        - ind 3, found that the first number < than itself is at ind 2
            - take the dp value at ind 2 and add to current pos
        [10,9,2,5,3,7,101,18]
        [1 ,1,1,2,1,1, 1 , 1]
        - ind 4, found that the first number < than itself is at ind 2
            - take the dp value at ind 2 and add to current pos
        [1 ,1,1,2,2,1, 1 , 1]
        - ind, first < number is at ind

        - issue if we have a longer subsequence before the first one
        [10,9,2,4,5,3,7,101,18]
        [1 ,1,1,2,3,2,1, 1 , 1]

        - so need to go through every number in dp

        Time: O(n^2)
        Space: O(n)
        '''
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
