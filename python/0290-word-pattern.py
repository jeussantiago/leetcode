class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        T: O(n)
        S: O(n)
        '''
        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        pat_char_key = {}
        pat_word_key = {}
        for char, word in zip(pattern, s):
            if word in pat_word_key and pat_word_key[word] != char:
                return False

            if char in pat_char_key and pat_char_key[char] != word:
                return False

            pat_word_key[word] = char
            pat_char_key[char] = word

        return True
