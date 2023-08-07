# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    '''
    [0, 1, 2, 3, 4, 5, 6]
    [7, 8, 9, 0, 1, 2, 3]
    [4, 5, 6, 7, 8, 9, 0]
    [1, 2, 3, 4, 5, 6, 7]
    [8, 9, 0, 1, 2, 3, 4]
    [5, 6, 7, 8, 9, 0, 1]
    [2, 3, 4, 5, 6, 7, 8]

    row_length = 7
    col_length = 7
    - increment each position from 1-10, repeating

    - get a row from rand7
    - get a col from rand7
    - using those row, col positions, we can go to the matrix and grab the rand10 value from there

    Issue:
        - the last set of numbers doesn't fully cover 1-10 (it doesn't cover the 9)
        - so if row == 6 or row==5 and col >=5
            - try again

    Time: avg   O(1)
        : worst O(inf) - happens if on the last row cause last row doesnt fully encapsulate the range of 1-10
    Space: O(1)
        ; 2d matrix but we know the size of it O(49)
    '''

    def __init__(self):
        self.table = [[None for _ in range(7)] for _ in range(7)]
        num = 0
        for row in range(7):
            for col in range(7):
                self.table[row][col] = num % 10
                num += 1

        for d in self.table:
            print(d)

    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # rand7 returns int 1-7, but need 0 index for matrix so -1
            row, col = rand7() - 1, rand7() - 1
            if row == 6 or (row == 5 and col >= 5):
                continue

            # get 0 but need 1, get 9 but need 10 - add 1
            return self.table[row][col] + 1
