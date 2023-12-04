class Solution:
    def largestGoodInteger(self, num: str) -> str:
        '''
        This code is so bad

        Time: O(n)
        Space: O(1)
        '''
        max_good = float('-inf')
        prev_num, consecutive_cnt = "", 0
        for char in num:
            if char == prev_num:
                consecutive_cnt += 1
            else:
                prev_num = char
                consecutive_cnt = 1

            if consecutive_cnt == 3:
                if int(prev_num) > max_good:
                    max_good = int(prev_num)
                else:
                    prev_num = char
                    consecutive_cnt = 1

        return str(max_good) * 3 if max_good != float('-inf') else ""
