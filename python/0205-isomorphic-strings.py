class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        - isomorphic means that each character matches to a single character
        - no two character match to the same characters

        - for each character in s, store it in a hash table
        - if the current character is not in the hash table
            - make the s character the key and corresponding t character the value
            - also check if character in t already has a matching character in s
        - if the current character is in the hash table
            - check if the hash value matches the corresponding character in t

        Time: O(n)
        Space: O(n)
        '''
        match = {}
        i = 0
        while i < len(s):
            c1 = s[i]
            c2 = t[i]
            if c1 not in match:
                if c2 in match.values():
                    return False
                match[c1] = c2
            else:
                stored_char = match[c1]
                if stored_char != c2:
                    return False

            i += 1

        return True
