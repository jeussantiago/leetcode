class WordDistance:
    '''
    ["practice", "makes", "perfect", "coding", "makes"]

    Init:

    store the word index in an list with keys to the word
    {
        "practice" : [0] 
        "makes" : [1,4]
        "perfect" : [2]
        "coding" : [3]
    }
    Time: O(n)
    Space: O(n)

    Shortest:

    - no indexes are repeating
    - each list is in order
    (we can advance the pointer on each node but seeing which value is smaller)

    Time: O(n + m) where n is number of times the word1 shows up in the wordsDict. but since its kept in a list, you
    just go through the list. M is the same for word2
    Space: O()

    '''

    def __init__(self, wordsDict: List[str]):
        self.wordIndexes = collections.defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.wordIndexes[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1Indexes = self.wordIndexes[word1]
        word2Indexes = self.wordIndexes[word2]

        N, M = len(word1Indexes), len(word2Indexes)
        minDistance = float('inf')
        i1, i2 = 0, 0
        while i1 < N and i2 < M:
            minDistance = min(minDistance, abs(
                word1Indexes[i1] - word2Indexes[i2]))

            if word1Indexes[i1] < word2Indexes[i2]:
                i1 += 1
            else:
                i2 += 1

        return minDistance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
