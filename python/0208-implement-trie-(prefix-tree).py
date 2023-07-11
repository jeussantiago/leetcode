class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    '''
    Prefix Tree is a word search algorithm
    (some applications are autocompelte and spellchecker)

    init
        - have a dictionary to store the 26 letters at each level
        - a boolean signifying the end of a word
        (this shows that a word exist and distinguishes self.search and self.startswith)

    [app, apc, add]
              a
      p             d

    c    p          d

    insert
        - go through the letters of the word
            - if the letter not in dictionary
                - create a dict (trie node) at the letter node
            - move pointer to lettter node
        - to signify that this is the end of a word, set a boolean for the node to True

    search
    - go through all characters in the word and if midway it stops (there is an empty dictionary or is empty in the
    letter node positin,)=> word doesn't exist
    - the word may not be in the dictionary but is just a prefix so to differentiate,
    check the boolean since if it is true, then that word had to be inserted before
    (if its false then that means that there is a longer word with this word as a prefix - this is still false in
    this case since it is not a word itself)

        - go through the letters of the word
            - if letter not in dict keys
                - return False (word not in dictionary)
            - move pointer to next letter

        - successfully went through the word
        - check if the current pointer shows that this is a word in the dicitonary

    startswith
    - similar to search except that you don't have care if the prefix is a prefix or a word, 
    - just return true if you're able to find the sequence of letters in the dictionary
        - operation the same as search


    Overall alogrithm
    Time: O(n)
    Space: O(26^m) 26 decisions each time and m in the height of the tree which is the longest word
    '''

    def __init__(self):
        # Time: O(1)
        # Space: O(1)

        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time: O(n) where n is the length of the word
        # Space: O(n)

        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Time: O(n) where n is the length of the word
        # Space: O(n)

        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]

        # check if the word was inserted before
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Time: O(n) where n is the length of the word
        # Space: O(n)

        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
