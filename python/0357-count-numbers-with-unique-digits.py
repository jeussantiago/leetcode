class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        10
        9

        91
        72
        - for the first digit, we have 9 options [1 to 9] = 9
        - for the second digit, we have 9 options as well(since we cant start a number with 0) [0,9] => 81 = previous_cnt * curr_num_options = 9 * 9
        - for the third digit, we have 8 options : 123 third digit had a positibility to be [0,3,4,5,6,7,8,9] => 648 = previous_cnt * curr_num_options = 81 * 8
        - for the fourth digit, we have 7 options : 1234 fourth digit had a posibilyt to be [0,4,5,6,7,8,9] => 4536 = previous_cnt * curr_num_options = 648 * 7
        ...and so on

        Time: O(n)
        Space: O(n)
        '''
        if n == 0:
            return 1

        # have to start at second digit since the first and second have the same number of options
        dp = [1, 9]
        options_cnt = 9
        n -= 1
        while n > 0:
            # each iteration shows how many numbers with unique nums that have n len digits
            dp.append(dp[-1] * options_cnt)
            options_cnt -= 1
            n -= 1

        return sum(dp)
