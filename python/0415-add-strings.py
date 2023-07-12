class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        Time: O(max(num1, num2))
        Space: O(1)
        '''
        res = []
        carry = 0
        i1, i2 = len(num1)-1, len(num2)-1
        while i1 >= 0 or i2 >= 0:
            n1 = int(num1[i1]) if i1 >= 0 else 0
            n2 = int(num2[i2]) if i2 >= 0 else 0
            val = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10

            res.append(val)

            i1 -= 1
            i2 -= 1

        if carry:
            res.append(carry)

        return "".join([str(num)for num in res[::-1]])
