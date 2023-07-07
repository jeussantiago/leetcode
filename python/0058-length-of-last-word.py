class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        Time: O(n + n) -> split is n time and then we go to each word and check if its not empty which is also n
            : O(n)
        Space: O(n) create space for length of string to split then create new array to store teh words without the empty spaces 
        '''
        words = [word for word in s.split(" ") if word]
        return len(words[-1])