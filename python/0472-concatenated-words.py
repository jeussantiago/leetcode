class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        for each position in the word, start the substring from the last possible instances of True (signifiying seen in the words list)
            - if the substring is found in the words list then put a true
            - otherwise false

        n is the length of the words list
        m is the length of each word
        Time: O(n * m^2)
            ; (n) go through each word
            ; (m) go through the characters of the word
            ; (m) check if the substring appears from the last time the word position was True
        Space: O(n + m)
            ; (n) hashset
            ; (m) the same variable gets reset everytime to be the length of the word
        '''
        res = []
        wordSet = set(words)
        for word in words:
            dp = [False] * (len(word) + 1)
            dp[0] = True
            wordSet.remove(word)
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j: i] in wordSet:
                        dp[i] = True

            wordSet.add(word)

            if dp[-1]:
                res.append(word)

        return res
