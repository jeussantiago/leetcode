class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        1 pass sliding window

        - keep a count of how many times a character has been seen
        - its fine for any given character to go above k
            - this means that, the 1 character above k is the longest sequence
            - the other would be assumed to be the changeable char
        - its not fine for both characters to go above k
            - if both are over, then it is not a valid substring anymore
            - have to reduce one of the characters to be below k
                - move the left pointer until one of the character is below k

        Time: O(n)
        Space: O(1)
        '''
        longestConsecutive = 0
        cnt = collections.defaultdict(int)
        l = 0
        for r in range(len(answerKey)):
            cnt[answerKey[r]] += 1

            if cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[l]] -= 1
                l += 1

            longestConsecutive = max(longestConsecutive, r - l + 1)

        return longestConsecutive


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        2 pass sliding window
            - in the first pass, see max number of True
            - in the second pass, see max number of False

        True pass:

        "TTTFFTTFFFTTTFF" ; k = 2
        - as you progress the sliding window, you can only accept k amount of "F"s
        'TTT' accept 'FF', k=0
        keep pushing right pointer
        'TTTFFTT'
        hit an F, but your k=0, so you start moving the left pointer until k != 0
        'FTTF' -> TTFF

        - at each loop, record the length of the valid substring

        Time: O(n)
            ; (2n) sliding window (left and right pointer)
            ; do the sliding window twice for both values in the answer key (T or F)
            ; (2 * 2n)
        Space: O(1)
            ; no extra space used
        '''

        def consecutiveChar(char):
            longestConsecutive = 0
            allowed = k

            l = 0
            for r in range(len(answerKey)):
                if answerKey[r] != char:
                    allowed -= 1

                while l < r and allowed < 0:
                    if answerKey[l] != char:
                        allowed += 1
                    l += 1

                longestConsecutive = max(longestConsecutive, r - l + 1)

            return longestConsecutive

        return max(consecutiveChar('T'), consecutiveChar('F'))
