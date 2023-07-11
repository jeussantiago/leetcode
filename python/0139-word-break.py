class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        s = "leetcode", wordDict = ["leet","code"]
        [T,F,F,F,F,F,F,F]

        - double loop through each character
        - if the substring from the start indx to the end indx is in the wordDict, then fill in
        the dp position ending to True
            - we can skip over characters in the string where the position in the dp array is false
            - we do this cause theres no point checking those in characters with no words in the dict

        [T,F,F,F,F,F,F,F,F]
           l e e t c o d e
        [T,F,F,F,T,F,F,F,F]
        [T,F,F,F,T,F,F,F,T]
        results = True

        s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        [T,F,F,F,F,F,F,F,F,F]
           c a t s a n d o g
        [T,F,F,T,T,F,F,F,F,F] - cat, cats
        [T,F,F,T,T,F,F,T,F,F] - sand
        [T,F,F,T,T,F,F,T,F,F] - and
        - we check for the next character "o" but nothing start's with the character
        - that's why the ending is False
        results = False

        Time: O(n^2)
        Space: O(n)
        '''

        # change list to set cause looking up variables in set is avg: O(1) while list is O(n)
        wordSet = set(wordDict)
        N = len(s)
        dp = [False for _ in range(N+1)]
        dp[0] = True

        for start in range(N):
            # skip over the characters that don't start after a word
            if not dp[start]:
                continue

            # go through every substrinng and check if its in the set
            for end in range(start+1, N+1):
                if s[start: end] in wordSet:
                    dp[end] = True

        return dp[-1]
