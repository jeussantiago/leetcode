class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        1) only search the string up until the 2nd str fits into the first. no needless searching
            - bussadis and sad => would only serach up to index 5 in this case or len(bussadis) - len(sad)
        2) keep checking until the currently letter is the first letter in the word
            => check for s in sadbutis
        2.1) another option is to check the substring
        3) once that is found, we keep checking the string for matching letters to the word
        4) otherwise we update the pointer and keep serearching

        Time: O(n)
        Space: O(1)
        '''
        if len(needle) > len(haystack) or not needle or not haystack:
            return -1

        i = 0
        #otuter loop stops if the word doesnt fit into the bigger word but innner loop keeps going if it does
        while i < (len(haystack) - len(needle)) + 1:
            if haystack[i] == needle[0]:
                #check substring
                haystackWord = haystack[i:i+len(needle)]
                if haystackWord == needle:
                    return i
            i += 1
        return -1

