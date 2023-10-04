class Solution:
    def magicalString(self, n: int) -> int:
        '''
        if the last char == 1, the next char has to be 2
        if the last char == 2, the next char has to be 1

        - how often they appear (1 or 2) depends on the index of your pointer

        - keep track of how many 1s

        Time: O(n)
            ; (n or logn) doubling or increasing by singles
        Space: O(n)
            ; (n) size is going to double the size of n since it increase by 2 or 1
        '''

        s = "122"
        ind = 2
        while len(s) < n:
            nextChar = "1" if s[-1] == "2" else "2"
            s += nextChar * int(s[ind])
            ind += 1

        return s[:n].count("1")
