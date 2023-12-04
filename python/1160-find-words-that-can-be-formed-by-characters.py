class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
            ; only space we need is for the counter for variable
            ; chars. There are a maximum of 26 unique letters
            ; in the string
        '''
        def is_subset(word, count):
            cnt = count.copy()
            for char in word:
                if (char not in cnt or
                        cnt[char] == 0):
                    return False

                cnt[char] -= 1

            return True

        res = 0
        count = collections.Counter(chars)
        for word in words:
            if is_subset(word, count):
                res += len(word)

        return res
