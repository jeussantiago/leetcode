class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        Recursion

        - go to every next jump of the knight
        - we will only visit each position w/ accompaniying remaining jumps once
        - the position will tell us the number of unique movements possible

        k is the number of possible number values
        Time: O(n)  
            ; (n * k) since k is a constant value from 0-9, it is reduced to (n)
        Space: O(n)
            ; recurison stack
            ; (n) stack
            ; (1) jumps adjacency list
        '''
        MOD = 10 ** 9 + 7
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        cache = collections.defaultdict(int)

        def getUniqueJumps(square, remainingJumps):
            if remainingJumps == 0:
                return 1

            if (square, remainingJumps) in cache:
                return cache[(square, remainingJumps)]

            res = 0
            for nextSquare in jumps[square]:
                res = (res + getUniqueJumps(nextSquare, remainingJumps - 1)) % MOD

            cache[(square, remainingJumps)] = res
            return cache[(square, remainingJumps)]

        res = 0
        for square in range(10):
            res = (res + getUniqueJumps(square, n - 1)) % MOD

        return res


class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        DP w/ space optimization

        - can convert to DP where columns are the square numbers and the rows and the
        current number of jumps

            0 1 2 3 4 5 6 7 8 9
          0
          1
          2

        - fill in the dp, the value of the box is going to be the previous box of the possible
        jumps of the current square
        - the first layer at remainingJumps=0 is going to be filled with 1s
        - this method converts recursion to dp but doesnt space optimize
        - to space optimize, we can not keep in space the entire 2d array
            - the only rows we care about are the current jump and the previous jump
            - each of those will be length 10 so we just need to remember those

        Time: O(n) 
        Space: O(1)
        '''

        MOD = 10 ** 9 + 7
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        if n == 1:
            return 10

        prevJumps = [1] * 10
        for _ in range(n - 1):
            currJumps = [0] * 10
            for square in range(10):
                numUniqueJumps = 0
                for nextJump in jumps[square]:
                    numUniqueJumps = (
                        numUniqueJumps + prevJumps[nextJump]) % MOD
                currJumps[square] = numUniqueJumps
            prevJumps = currJumps

        return sum(currJumps) % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        FINDING A PATTERN

        1 2 3       A B A
        4 5 6   =>  C E C
        7 8 9       A B A
          0           D

        - certain positions have the same jump positions
        - positions 1,3,7,9 will be group A
        - positions 2,5 will be group B
        - positions 4,6 will be group C
        - positions 0 will be group D
        - positions 5 will be group E

        - A will always jump to  2 B or 2 C 
        - B will always jump to A
        - C will always jump to 2 A and 1 D 
        - D will always jump to C
        - E wont jump

        - now we just need to simulate starting from those group positions

        Time: O(n)
            ; same runtime but much faster b/c of less overhead
        Space: O(1)
        '''
        if n == 1:
            return 10

        MOD = 10 ** 9 + 7
        # number of times the square appears in the groups
        A = 4
        B = 2
        C = 2
        D = 1

        # go through each jump
        for _ in range(n - 1):
            A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C

        return (A + B + C + D) % MOD
