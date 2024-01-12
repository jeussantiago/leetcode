class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        '''
        Time: O(n)
        Space: (n)
            ; can optimize to O(1) by using pointers
        '''
        n = len(s)
        half = n // 2
        left, right = s[:half], s[half:]
        left_count, right_count = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for c in left:
            if c in vowels:
                left_count += 1

        for c in right:
            if c in vowels:
                right_count += 1

        return left_count == right_count
