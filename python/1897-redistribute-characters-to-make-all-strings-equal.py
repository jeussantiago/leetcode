class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        '''
        n is the length of words array
        k is the avg length of each word
        Time: O(n * k)
        Space: O(1)
            ; (26) hash map will contain only 26 alphabet letters
        '''
        cnt = collections.defaultdict(int)
        for word in words:
            for c in word:
                cnt[c] += 1

        for num in cnt.values():
            if num % len(words) != 0:
                return False

        return True
