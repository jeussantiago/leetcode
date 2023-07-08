class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        [9,9,9] = [1,0,0,0]

        Time: O(n)
        Space: O(n) - n + 1 for modifying digits array
        '''
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 0:
                break
            added_num = digits[i] + carry
            digits[i] = added_num % 10
            carry = added_num // 10
            
        if carry:
            digits.insert(0, carry)

        return digits
        