class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        - can't remove 1 element
        - 1 operatrions to remove 2-3 elements (2)
        - 2 operatrions to remove 4-6 elements (3)
        - 3 operatrions to remove 7-10 elements (4)

        Time: O(n)
        Space: O(n)
        '''
        counter = collections.Counter(nums)
        print(counter)
        res = 0
        for cnt in counter.values():
            if cnt == 1:
                return -1
            res += ceil(cnt / 3)

        return res
