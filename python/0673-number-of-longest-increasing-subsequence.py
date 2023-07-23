class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        - go back on itself
        - store the length of its sequences
        nums = [1,3,5,4,7]
        [(1,1), (2,1), (3,1), (3,1), (3,2)]

        - if its length >, 
            - increase current length +1
            - we take on that countvalue
        - if its length ==, 
            - we add the count to the current count

        Time: O(n^2)
        Space: O(n^2)
        '''
        n = len(nums)
        # length of sequence, count
        length = [1] * n
        count = [1] * n

        max_length = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

            max_length = max(max_length, length[i])

        count_increasing_subsequence = 0
        for i in range(len(length)):
            if length[i] == max_length:
                count_increasing_subsequence += count[i]

        return count_increasing_subsequence
