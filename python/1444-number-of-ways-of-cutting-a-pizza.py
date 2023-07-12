class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        '''
        T: O(k * n^4)
        S: O(n^2)
        '''
        # for d in pizza:
        #     print(d)
        # print('----')

        rows = len(pizza)
        cols = len(pizza[0])

        # Initialize a 2D array to store the number of 'A' toppings in each sub-rectangle of the pizza
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                total_apples = (apples[row + 1][col]
                                + apples[row][col + 1]
                                - apples[row + 1][col + 1])
                if pizza[row][col] == "A":
                    total_apples += 1

                apples[row][col] = total_apples

        # for d in apples:
        #     print(d)
        # print('----')

        # number of ways to cut a pizza into 1 pice
        f = []
        for row in range(rows):
            f.append([int(apples[row][col] > 0) for col in range(cols)])

        # def x():
        #     for d in f:
        #         print(d)
        #     print('==========')

        mod = 1000000007

        for remain in range(1, k):
            # x()
            g = [[0 for col in range(cols)] for row in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    # calculate number of ways to cut the pizza into k pieces
                    # after each cut, look at the next row/col
                    # the next row/col will tell us if there apples remaining in both slices
                    # if there are apples remaining, this means this is another way to cut a piece into k pieces
                    # do for all the next rows/cols
                    for next_row in range(row + 1, rows):
                        if apples[row][col] - apples[next_row][col] > 0:
                            g[row][col] += f[next_row][col]
                    # print(row, col, g[row][col])
                    for next_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            g[row][col] += f[row][next_col]

                    # print(row, col, g[row][col])
                    # print('---')
                    g[row][col] %= mod
            f = g

        return f[0][0]
