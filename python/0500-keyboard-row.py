class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        '''
        Time: O(n)
            ; turn each word into a set
            ; check if set is a subset of each row
        Space: O(1)
            ; (3) set for each row of the keyboard
        '''

        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        keyboard_rows = [first_row, second_row, third_row]
        res = []
        for word in words:
            set_word = set(word.lower())
            for row in keyboard_rows:
                if set_word.issubset(row):
                    res.append(word)

        return res
