class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    '''
    prefix tree

    init:
        - initialize a tree node
            - tree node has dictionary for each letter character
            - boolean for endOfWord

        Time: O(1)
        Space: O(1)

    addWord:
        - go through each character in word
            - traverse through the dictionary at the character positions
            - if the character as a key doesn't havle a node,
                - create a new node at that character key position

            - move the pointer to the next character position

        - end of word/ pointer is at the last letter
        - endOfWord = True

    Time: O(n)
    Space: O(n)

    search:
        - recursion, using the index and the pointer

        - if index >= len(word):
            - make sure that the current pointer is at the end of a word
            - if curr pointer.endOfWord == True
                return True
            - otherwise it is not the end of a word
                return False

        - go to the next character
            - if character == "."
                - traverse through all the available characters
                for possible_c in pointer.children:
                    dfs(i+1, pointer.children[possible_c])

            - if character is a letter
                - if character not in dictionary:
                    return False since the word can't be found
                - move pointer to character positions
                dfs(i+1, pointer.children[word[i]])
        - return True

    Time: O(26^n) where is the length of the word
    Space: O(m) where m is the number of words inserted

    Overall:
    Time: (26^n)
    Space: O(26^n) 26 choices in tree, height n would be the average length of a word

    '''

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(i, cur):
            if i >= len(word):
                return cur.endOfWord

            c = word[i]
            if c == ".":
                for possible_c in cur.children:
                    if dfs(i+1, cur.children[possible_c]):
                        return True
            else:
                if c not in cur.children:
                    return False
                if dfs(i+1, cur.children[c]):
                    return True

        cur = self.root
        res = dfs(0, cur)
        return res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
