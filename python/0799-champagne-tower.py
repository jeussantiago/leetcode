class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        we can simulate pouring the champagne. Instead of pouring one by one, we pour all the chamnpagne onto the top cup.

        - for each cup, subtract -1 from the current volume of the cup to account for the cup being fully filled
        - then divide that amount by 2 to signify spilling evenly onto the left or right side
        - the left sdie will pour onto (row + 1, col) and the right side will pour onto (row + 1, col + 1)

        R is the number of rows (query_row)
        Time: O(R ^ 2)
            ; each row will have the same number of glasses as the row number (R * R)
        Space: O(R ^ 2)
            ; we have to store the 2d array of size R * R
        '''
        # create champagne tower
        tower = [[0] * (row + 1) for row in range(query_row + 1)]
        # simulate powering onto the towere
        tower[0][0] = poured
        for row in range(query_row):
            for glass in range(row + 1):
                excess_champagne = (tower[row][glass] - 1) / 2.0
                if excess_champagne > 0:
                    tower[row + 1][glass] += excess_champagne
                    tower[row + 1][glass + 1] += excess_champagne

        # the glass might have much more champagne than it can hold. the max it can hold is 1.0
        return min(1.0, tower[-1][query_glass])
