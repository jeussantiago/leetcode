class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time: O(26 * n)
        Space: O(1)
            ; hashmap is size (26) for each letter
        '''
        count = collections.defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            # if the count shows "B": 3 and "A": 2 and "C": 1 with k = 2 and length of current substring = 6
            # it would be 6 - 3 = 3 ; this signifies that, for the longest continuos char in the substring, there are 3 chars that are not
            # equal to the longest count of character, in this case "B"
            # so you could replace those other characters. But since the count is > k, we have to start removing chars from the left side to get it under k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        time optimization 
            - don't have to look at the hash map every time
        Time: O(n)
        Space: O(1)
        '''
        count = collections.defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
