class Solution:
    def toHex(self, num: int) -> str:
        hex_convertion = '0123456789abcdef'
        res = ''

        # convert negative to positive/ 2's compliment
        if num < 0:
            num += (2 ** 32)
        elif num == 0:
            return '0'

        while num > 0:
            res += hex_convertion[num % 16]
            num //= 16

        return res[::-1]
