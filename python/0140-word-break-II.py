class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        recursion/ double loop

        - base case
            - start > len(s): add sentence to results

        - loop substring end (start+1, len(s))
            if s[start: end] in wordDict:
                function( new_start=end, sentence + " " + s[start : end] )

        Time: O()
        Space: O()
        '''

        res = []

        def helper(start, sentence):
            if start >= len(s):
                sentence = sentence[1:]
                res.append(sentence)
                return

            for end in range(start+1, len(s)+1):
                if s[start: end] in wordDict:
                    helper(end, sentence + " " + s[start: end])

        helper(0, "")
        return res
