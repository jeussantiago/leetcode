class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        cnt = collections.Counter(nums)

        max_freq = 0
        cnt_nums_with_max_freq = 0
        for num, freq in cnt.items():
            if freq > max_freq:
                max_freq = freq
                cnt_nums_with_max_freq = 1
            elif freq == max_freq:
                cnt_nums_with_max_freq += 1

        return max_freq * cnt_nums_with_max_freq
