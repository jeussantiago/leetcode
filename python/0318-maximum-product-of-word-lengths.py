class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        - comparing 2 sets
        set(a, b, c) & set(d,f,e) => set()
        set(a, b, d) & set(d,f,e) => set(d)

        - have to go through every combination of strings
        - if when you compare the sets and there is none in the left over set, this means that they do not shar a common letter

        Time: O(n^2 + L) where n is the number of words and L is the number of characters in all the words combined
        Space: O(n)
        '''

        # create a set for all the strings
        lookup = collections.defaultdict(set)
        for word in words:
            lookup[word] = set(word)

        def dont_share(word1, word2):
            if lookup[word1] & lookup[word2]:
                # non-empty set
                return False
            # empty set
            return True

        # compare string by string
        mx = 0
        for word1 in words:
            for word2 in words:
                if dont_share(word1, word2):
                    mx = max(mx, len(word1) * len(word2))

        return mx
