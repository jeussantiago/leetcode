class Solution:
    def grayCode(self, n: int) -> List[int]:
        '''
        create a string of 0 of length n
        create a list of every possible combination of 0 and 1

        - number of combinations = 2 ^ n


        Time: O()
        Space: O()
        '''

        res = []
        for i in range(1 << n):
            x = i ^ (i >> i)
            res.append(x)
        print(res)
