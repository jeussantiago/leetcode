class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        '''
        - first make sure that both indexes have something (neither is -1)

        - if you find a matching word
            - if both are -1
                - set index to one
            - if one is -1
                - set that one to the index
            - if both are not -1
                - whichever has the smaller index, update it to the current index

        ["makes", "perfect", "coding", 'perfect', 'perfect', 'makes',"makes", "coding", "perfect"]

        - if the previous index is a different word from the current index,
            - then culculate the difference

        - if you have repeating words -> its ok to update the index
        (distance would only be calculated at the positions  on words that are just before and after each other)
        (["coding", "makes" "makes", "makes", "coding"] )
            |           |
            calculates distance here
                        |       |
                        but these are the same words so no need to calculate
        (pretty muuch when it alternates)

        - this is for words that are different, if the words are the same, just calculate the distance

        Time: O(n)
        Space: O(1)
        '''

        minDistance = len(wordsDict) - 1
        prevIndex = -1
        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if prevIndex != -1 and (word1 == word2 or wordsDict[prevIndex] != wordsDict[i]):
                    #               same words           alternating words
                    minDistance = min(minDistance, i - prevIndex)

                prevIndex = i

        return minDistance
