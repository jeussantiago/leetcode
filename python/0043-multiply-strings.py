class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
                123
               x456
         ------------
                738 (multiply first position with everything)
                (5 digit - move over one 0 digit and multiple 5x3 and add it to currently number 3+15)
                => 6888
                => 56088
                ------------
                56088

        - largest a number can be is the len(num1) * len(num2) => Ex: 99*99 = 9801
        - reverse the numbers - want to work from ones position outwards
        - keep each number stored in a list
        - multiply numbers
        - add number to the value in the corresponding list
        - get the carry and add that to the next number
        - get the remainder of the carry and replace the current number with it


        Constraints:
        - can't turn strings in integer (doesn't mean we can't turn individual numbers into int - 
        we just can't go outside of the 32-bit range)
        - nums can be 0
        - nums contian digits only

        '''
        if '0' in [num1, num2]: return '0'

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                num = int(num1[i1]) * int(num2[i2]) #multiply
                res[i1 + i2] += num #add digit to position (added carry from previous loop iteration)
                res[i1 + i2 + 1] += res[i1 + i2] // 10 #carry
                res[i1 + i2] = res[i1 + i2] % 10 #remainder/last number
        # [8, 8, 7, 5, 4, 0]
        #values in list are int, need to convert them to str and join
        res, zero_ind = res[::-1], 0
        while zero_ind < len(res) and res[zero_ind] == 0:
            zero_ind += 1
        return "".join(map(str, res[zero_ind:]))
        



