class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        '''
        2 pointers

        n is the length of word
        m is the length of abbr
        Time: O(n + m)
        Space: O(1)
        '''
        ptr1, ptr2 = 0, 0
        while ptr1 < len(word) and ptr2 < len(abbr):
            if abbr[ptr2].isdigit():
                # leading zero
                if abbr[ptr2] == '0':
                    return False

                # get the entire digit
                num = 0
                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    num = (num * 10) + int(abbr[ptr2])
                    ptr2 += 1

                ptr1 += num

            else:
                if word[ptr1] != abbr[ptr2]:
                    return False

                ptr1 += 1
                ptr2 += 1

        if ptr1 != len(word) or ptr2 != len(abbr):
            return False
        return True
