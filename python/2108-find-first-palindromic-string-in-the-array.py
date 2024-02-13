class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        '''
        n is the length of words array
        k is the length of the longest word
        Time: O(n * k)
            ; (n) go to each word in array
            ; (k) each word, you have to reverse
        Space: O(1)
        '''
        for word in words:
            if word == word[::-1]:
                return word

        return ""
