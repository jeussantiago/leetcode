
class TrieNode:
    def __init__(self):
        self.children = {}
        self.ind = -1
        self.palindromeSuffixes = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def isPalindrome(word):
        return word == word[::-1]

    def insert(self, word, i):
        node = self.root
        word = word[::-1]
        for j, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()

            if self.isPalindrome(word[j:]):
                node.palindromeSuffixes.append(i)

            node = node.children[c]
        node.ind = i

    def insertWords(self, words):
        for i, word in enumerate(words):
            self.insert(word, i)

    def search(self, word, i):
        pairs = []
        node = self.root

        for j, c in enumerate(word):
            # first word is >= len of second word
            # end of a word, make sure that the end of the current word is a palindrome
            # Ex: B and NAB are in the Trie ; compare with BANANA
            if node.ind != -1 and self.isPalindrome(word[j:]):
                pairs.append([i, node.ind])

            if c not in node.children:
                return pairs

            node = node.children[c]

        # reached end of word, check to see if current node is the reverse of the word by seeing if it has an index
        if node.ind != -1 and node.ind != i:
            pairs.append([i, node.ind])

        # check for palindromes at the end of - case of first word shorter than longer words
        for j_ind in node.palindromeSuffixes:
            pairs.append([i, j_ind])

        return pairs


class Solution:
    '''
    [CAT, LILCAT, BIGCAT, LOLCAT, BANANA, B, BAN]

    "aaaacat"
    - we have to check if [:i] is a palindrome
        ""
        "a"
        "aa"
        "aaa"    
        "aaaa"
        - these are all palindromes
        - check the reverse of the following chars in the hash map
        ""      ; check -> "tacaaaa"
        "a"     ; check -> "tacaaa"
        "aa"    ; check -> "tacaa"
        "aaa"   ; check -> "taca"
        "aaaa"  ; check -> "tac"


    - go through every word
        - go through every index of the word
            - check if the word at the index is a palindrome
                - if it is a palindrome
                    - check to see if the reverse is in the Trie
                    - if the reverse is in the, put the found word index in front
                    ( this would require us to insert every index combination in the hash map )

    [abcd, dcba, lls, s, sssll]
    a   b   c   d

    d   c   b   a

    l   l   s

    s   s   s   l   l   

    (n is the len of words and k is the leng of the max len word)
    Time: O(n * k^2) put the words in the trie (n * k);
                    iterate over each word again, at each index (n)
                        - check if palindrome O(k)
                            - check if word in Trie O(k) 
    Space: O(n^2 * k) ; the trie will have all the possible letters
                      ; each node might have up to n indexes in it's list
    '''

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        root.insertWords(words)
        res = []
        for i, word in enumerate(words):
            pairs = root.search(word, i)
            res.extend(pairs)

        return res

    def isPalindrome(self, word: str) -> bool:
        return word == word[::-1]
