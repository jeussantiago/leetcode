class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWordCount = 0
        self.prefixCount = 0


class Trie:
    '''
    each position contains:
        - (char)
        - EndOfWordCount (keep track if the word exist completely) - int
        - prefixCount (keep track of how many times the prefix appears in otehr words) - int

    insert:
        - if the position doesnt exist, create the new Trie node
        - increase EndOfWordCount + 1
        - increase prefixCount + 1

    countWordsEqualTo:
        - looking for if word even exist in Trie
        - if exist, return EndOfWordCount
    countWordsStartingWith
        - looking for if word even exist in Trie
        - if exist, return prefixCount

    erase (guranteed that the word will already exist in the Trie)
        - go to each letter
            - reduce count of EndOfWordCount - 1
            - reduce count of prefixCount - 1

    n is the length of word
    m is the number of unique words
    Time: O(n)
    Space: O(m)
    '''

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.prefixCount += 1

        node.EndOfWordCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0

            node = node.children[char]

        return node.EndOfWordCount

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0

            node = node.children[char]

        return node.prefixCount

    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.prefixCount -= 1

        node.EndOfWordCount -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
