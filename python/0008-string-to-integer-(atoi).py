class Solution:
    def myAtoi(self, s: str) -> int:
        """
        1. whitespace
        2. leading +/- symbol
        3. numbers
        4. between max_int and min_int constraints
        5. random characters

        Time O(n)
        Space O(1)

        n is the number of characters in the string
        for space, res grows with the input but because it never grows passed the max or min_int, its constant space
        """

        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648

        i = 0
        res = 0
        negPos = 1

        #whtiespace
        while i < len(s) and s[i] == ' ':
            i += 1

        #leading +/- symbol
        if i < len(s) and s[i] == '-':
            i += 1
            negPos = -1
        elif i < len(s) and s[i] == '+':
            i += 1

        #numbers
        numChecker = set('0123456789')
        while i < len(s) and s[i] in numChecker:
            #make sure it doesnt leave constraints and overflows
            res = res * 10  + int(s[i])
            if res > MAX_INT:
                return MAX_INT if negPos == 1 else MIN_INT
            i += 1

        return res * negPos





