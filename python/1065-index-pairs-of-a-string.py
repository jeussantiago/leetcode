class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        '''
        Hash Set
        '''
        words, N = set(words), len(text)
        res = []
        for i in range(N):
            for j in range(i, N):
                if text[i:j+1] in words:
                    res.append([i, j])
        return res


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        '''
        Trie Solution

        text = "ababa", words = ["aba","ab"]
        - a dict containing a list of words that start with that character
        {"a": ["aba","ab"]}

        - when you get to a char in text, you can just go through the words in the dict and see if they match the next following chars

        - either sort the words based on length or sort the output

        Time: O(n^2)
        Space: O(n)
        '''

        start = collections.defaultdict(list)
        for word in words:
            start[word[0]].append(word)

        res = []
        for i, char in enumerate(text):
            if char in start:
                for word in start[char]:
                    sub = text[i: i+len(word)]
                    if word == sub:
                        res.append([i, i+len(word)-1])

        res.sort()
        return res
