class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_sum = int(a, 2) + int(b, 2) #turn binary string to numbers 
        bin_str = bin(int_sum) #turn number into binary string
        return bin_str[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        binary to number
        - 1010
        2^3 + 2^2 + 2^1 + 2^0
        8 + 4 + 2 + 1
        8 + 0 + 2 + 0
        = 10 (int value)

        number to binary
        - 10
        10 // 2 = 5
            5 % 2 = 1
        5 // 2 = 2
            2 % 2 = 0
        2 // 2 = 1
            1 % 2 = 1
        ==> 101 (binary) 

        '''
        def binaryToNum(bin):
            num = 0
            for i, n in enumerate(bin[::-1]):
                if n == '1':
                    num += (2 ** i)
            return num

        def numToBinary(num):
            bin = ""
            while num >= 1:
                n = num % 2
                num = num // 2
                bin = str(n) + bin
            if not bin:
                return "0"
            return bin
        
        int_sum = binaryToNum(a) + binaryToNum(b)
        return numToBinary(int_sum)

        