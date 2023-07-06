class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        #iterate through string by the number of rows
        #next letter = 2 * (numberOfRows - 1)
        #iterate thorugh rows starting at the current row until you go out of bounds in the string, increment by the calculated next letter
        #add value to the string (this method only works for the first and last row since theyre the onyl ones with 2 letters in a zigzag)
        res = ""
        for r in range(numRows):
            #only works for top and bottom of zigzag
            increment = 2 * (numRows - 1) #where the next letter is
            for i in range(r, len(s), increment):
                res += s[i]
                #middle rows only
                #as we go lower in the rows, the size of the zigzag decreses by 2
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)): #check if there is still a letter within contraints
                    res += s[i + increment - (2 * r)]
        return res
