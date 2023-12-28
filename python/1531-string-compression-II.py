class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        '''
        Time: O(n^2 * k)
            ; (n) i can be of length n
            ; (k) k can be at most k
            ; (26) prev_char can be at most 26 possible characters, letters 
            ; (n) prev_cnt can be at most n size
            ; => n * k * 26 * n
        Space: O(n^2 * k)
        '''

        cache = {}

        def compress(i, k, prev_char, prev_cnt):
            if i == len(s):
                return 0

            if (i, k, prev_char, prev_cnt) in cache:
                return cache[(i, k, prev_char, prev_cnt)]

            if prev_char == s[i]:
                # continueing char
                # 1 -> 2 ; a -> a2
                # 9 -> 10 ; a9 -> a10
                # 99 -> 100 ; a99 -> a100
                # these prev_cnt values change the length of the results
                inc = 1 if prev_cnt + 1 in [2, 10, 100] else 0
                res = inc + compress(i+1, k, s[i], prev_cnt + 1)
            else:
                # different character
                option_one = float('inf')
                if k > 0:
                    # delete the current character
                    option_one = compress(i+1, k-1, prev_char, prev_cnt)

                # don't delete the current character - changed chars, increase result
                option_two = 1 + compress(i+1, k, s[i], 1)
                res = min(option_one, option_two)

            cache[(i, k, prev_char, prev_cnt)] = res
            return res

        return compress(0, k, "", 0)
