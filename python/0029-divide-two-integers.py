class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        - can't use * / and % 
        - keep subtracting
        - exponentially increase divisor by itself
        - can't multiply by 2 so add it to itself

        Time: O(log(n))
        '''
        dvnd = abs(dividend)
        dvsr = abs(divisor)

        output = 0
        while dvnd >= dvsr:
            tmp = dvsr
            mul = 1
            while dvnd >= tmp:
                dvnd -= tmp
                output += mul
                mul += mul
                tmp += tmp
        
        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            output = -output
        return min(2147483647, max(-2147483648, output))

    '''
    dividend = 25  divisor = 3
    -----------
    mul = 1
    tmp = 3
    dvnd = 22
    output = 1

    mul = 2
    tmp = 6
    dvnd = 16
    output = 3

    mul = 4
    tmp = 12
    dvnd = 4
    output = 7

    mul = 8
    tmp = 24

    (dvnd >= temp : breaks out of inner loop but keeps going because dvnd is still greater than dvsr)
    mul = 1
    tmp = 3
    dvnd = 1 = (4-3)
    output = 8 = (7 + 1)

    mul = 2
    tmp = 6
    
    (dvnd >= tmp: breaks cause not true anymore ; dvnd >= dvsr : breaks cause not true anymore)

    output = 8

    '''

