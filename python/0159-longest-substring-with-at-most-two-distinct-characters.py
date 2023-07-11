class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        ececddd

        - one pointer -> iterating through teh entire array
        - one pointer (trailing) -> deleting/subtracting count of the letters

        - counter dictionary

        if len(counter) < 2:
            - add letter to dictionary
            - counter[letter] += 1
            - store the max length

        len(counter) >= 2
        (get rid of trailing letters)
            (another possible place to store the max lenght)

            while len(counter > 2)
            - subtract the count of the trailing counter

            - if any letter hits 0, remove it from the keys/set

            - increase trailing counter index

        Time: O(n)
        Space: O(n)
        '''
        res = 1
        counter = collections.defaultdict(int)
        trailing_indx = 0
        for leading_indx, leading_c in enumerate(s):
            counter[leading_c] += 1

            while len(counter) > 2:
                trailing_c = s[trailing_indx]
                counter[trailing_c] -= 1
                if counter[trailing_c] == 0:
                    counter.pop(trailing_c)
                trailing_indx += 1

            res = max(res, leading_indx - trailing_indx + 1)

        return res
