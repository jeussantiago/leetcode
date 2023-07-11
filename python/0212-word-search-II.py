class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.letterOccurrence = 0

    def createTree(self, words):
        for word in words:
            node = self
            node.letterOccurrence += 1
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.letterOccurrence += 1
            node.endOfWord = True

    def removeWord(self, word):
        node = self
        node.letterOccurrence -= 1
        for c in word:
            node = node.children[c]
            node.letterOccurrence -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        - create a Trie Tree with the words
        - a string at the end of the word that signifies that it is the end, the 
        content of the string is the word itself

        words = [eat, pea]

                    {}
                e           p
            a            e
        t           a

        - go through each cell,
            - dfs(current position using row and col, root pointer of tree)

        DFS:
        - need some way to stop going over repeated characters and symbols -> keep track of how many times a letter appears with a prefix
            - have counter on each node to represent how many times that letter  in that position in the tree should appear
            (this would solve the problem of repeated work since we can just skip over repeating words with the same prefix
            i.e. [abababaa, abababab])
            - when we add a wordto results, we need to reduce the amount of the counter at each letter for the word

        - if position not in bounds or
          position not in visited cell set or
          current cell character is not in the curr branch of keys/letters:
            return

        - elif character in curr branch of keys/letters
            - check if its the end of the word
            - if it is the end of the word, append the word to the results
            (don't return, there might be a longer string with the same characters i.e. [do, door])


        dfs(horizontal and vertical positions, visited cell set)


        Time: O(m*n * w) where w is the length of a word
        Space: O(p*w * 26^w) where w is the length of the word and p is the length of words (for the set)
        '''
        root = TrieNode()
        root.createTree(words)

        res, visited = set(), set()
        M, N = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col, node, word):
            if (
                row not in range(M) or
                col not in range(N) or
                (row, col) in visited or
                board[row][col] not in node.children or
                node.children[board[row][col]].letterOccurrence < 1
            ):
                return

            c = board[row][col]
            node = node.children[c]
            word += c
            if node.endOfWord:
                res.add(word)
                root.removeWord(word)
                node.endOfWord = False

            visited.add((row, col))
            for rowDir, colDir in directions:
                dfs(row + rowDir, col + colDir, node, word)
            visited.remove((row, col))

        for row in range(M):
            for col in range(N):
                dfs(row, col, root, "")

        return list(res)
