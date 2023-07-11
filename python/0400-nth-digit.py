class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        num_of_digits = 1
        base_val = 9
        # number_of_digits -> 1, 2, 3, 4 ...
        # base of value -> 9, 90, 900, 9000, ...
        # combined value goes -> 9, 180, 2700, 36000

        while n > (base_val * num_of_digits):
            n -= (base_val * num_of_digits)
            num_of_digits += 1
            base_val *= 10

        n, ind_nth_digit = divmod((n-1), num_of_digits)
        res = 10 ** (num_of_digits - 1) + n
        print(res, ind_nth_digit, n, num_of_digits)
        return int(str(res)[ind_nth_digit])
