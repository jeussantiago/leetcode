class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        ransom = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)

        for key, val in ransom.items():
            if mag[key] < val:
                return False
        return True
