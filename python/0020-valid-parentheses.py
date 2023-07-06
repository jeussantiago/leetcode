class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1) string has to have atleast 1 charcter
        2) string only contains ()[]{}

        1. store all combinations in a hashtable - remove beginning cause we don't care so much
        about how we're starting
        2. a list containing the order the characters appear
        [({})]
        '''

        charsOpposite = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        charsOrder = [] 
        for c in s:
            #if the character is an ending one, check the last character within the array, if it is valid, then remove it, otherwise string is False
            if c in charsOpposite.values():
                #if it enters this if statement, for it to be valid, that means that there has to be a character already inserted
                if len(charsOrder) == 0:
                    return False
                lastChar = charsOrder.pop()
                if c != charsOpposite[lastChar]:
                    return False
            else:
                charsOrder.append(c)

        if len(charsOrder) > 0:
            return False
        return True


