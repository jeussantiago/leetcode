class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        - count the number of letters in s

        - go through all characters at t
            - at each charcter
            - if the character is not in the counting dict
                - return false

            if dict[char] <= 0:
            (the character is appearing too many times in t)
                - return false

            else
                - dict[char] -= 1

        - we need to check if any letter still has a count
        (i.e. s = door ; t = dr)


        Time: O(s + t)
        Space: O(max(s, t))
        '''
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1

        for c in t:
            if count[c] <= 0:
                return False
            else:
                count[c] -= 1

        return sum(count.values()) == 0
