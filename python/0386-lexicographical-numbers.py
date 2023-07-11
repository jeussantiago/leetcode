class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        '''
        n = 203
        [1,10,100,101,102...110,111,112,11,12,20,21,22,2]

        - 1 to 9 will take care of all values in n range

        - do 1,
            - able to multiply 1 by 10 and its under n
        - do 10, able to 

        Time: O(n)
        Space: O(n)
        '''
        res = []
        num = 1
        for _ in range(n):
            res.append(num)

            if num * 10 <= n:
                num *= 10
            elif num % 10 != 9 and num + 1 <= n:
                num += 1
            else:
                num //= 10
                while num % 10 == 9:
                    num //= 10
                num += 1
        return res
