class TrieNode:
    '''
    Time: O(1)
    Space: O(1)
    '''

    def __init__(self):
        self.children = {}
        self.prefixWords = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def buildTree(self, words):
        '''
        where n is the length of the words list
        where w is the length of the individual words
        Time: O(n * w)
        Space: O(n * w)
        '''
        for word in words:
            node = self.root
            for char in word:
                node.prefixWords.append(word)
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.prefixWords.append(word)

    def getPrefixWords(self, prefix):
        '''
        w is the lenght of the individual word (in this problem, all words are the same length)
        Time: O(w)
        Space: O(1) ; no extra space usage
        '''
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return node.prefixWords


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        ["area","lead","wall","lady","ball"]

        [
            [b , a , l , l]
            [a , r , e , a]
            [l , e , _ , _]
            [l , a , _ , _]
        ]

        - go through each word and see if the substring of the position matches the word to fill in

        Time: O(n * w)
        Space: O()
        '''

        trie = Trie()
        trie.buildTree(words)

        res = []

        def dfs(square):
            ind = len(square)
            if ind == len(words[0]):
                res.append(square)
                return

            # current position in square substring
            prefix_sub = "".join(word[ind] for word in square)

            for word in trie.getPrefixWords(prefix_sub):
                dfs(square + [word])

        dfs([])
        return res
