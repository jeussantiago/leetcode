class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        '''
        s is the length of sentence arr
        r is the length of rows
        c is the lenght of cols
        Time: O(s * c + r) ; worst case is that a sentence fits on an entire line
        Space: O(s * c)
        '''
        # sentence index, row index, col index
        n = len(sentence)

        # cache:
        # at the current i, starting from position 0 in the column
        # the cache will return what index we'll be on in the sentence at the end of this row/col==cols and
        # how many times the sentence fits into the row/col==cols
        @lru_cache(None)
        def dp(i):
            col, sentence_count = 0, 0

            while col + len(sentence[i]) <= cols:
                col += len(sentence[i]) + 1
                i += 1

                if i == n:
                    sentence_count += 1
                    i = 0

            return i, sentence_count

        res, i = 0, 0

        for _ in range(rows):
            ret = dp(i)
            res += ret[1]
            i = ret[0]

        return res
