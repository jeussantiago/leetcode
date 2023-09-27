class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        '''
        leet2code3

        1) string: l -> length: 1 
        2) string: le -> length: 2
        3) string: lee -> length: 3
        4) string: leet -> length: 4
        5) string: leetleet -> length: 8
        6) string: leetleetc -> length: 9   
        7) string: leetleetco -> length: 10
        8) string: leetleetcod -> length: 11
        9) string: leetleetcode -> length: 12
        10)string: leetleetcodeleetleetcodeleetleetcode -> length: 36  

        - since they're copies of each other, we geet
            leetleetcode-leetleetcode-leetleetcode
            - we can divide the length by the number 3 to get
            length 12 -> leetleetcode

        - the next character would be a letter so we can reduce the length by -1
            length 11 -> leetleetcod
        - reduce the length again since its a character
            length 10 -> leetleetco
        - length == k so we would return "o" but we will keep going for examples sake
        (speed through the remain letter and go to the digit)
            length 8 -> leetleet
        - current char is 2, so we divid the length by 2 
            length 4 -> leet

        Time: O(n)
        Space: O(1)
        '''

        decoded_length = 0
        # get the length of the full string
        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1

        # reverse search to find the kth character
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char.isdigit():
                decoded_length //= int(char)
                k %= decoded_length
            else:
                if k == 0 or k == decoded_length:
                    return char
                decoded_length -= 1

        return ""
