class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)
        c1, c2 = sorted(cnt1.values()), sorted(cnt2.values())
        # 1) have to make sure they have the same characters and length of strings
        # dict_keys(['a', 'b', 'z', 'c']) dict_keys(['b', 'a', 'z', 'c'])
        # 2) turning all of the same characters into another char and vice versa
        # Ex: abb => baa
        # [1, 2, 2, 2] [1, 1, 2, 3]
        return cnt1.keys() == cnt2.keys() and c1 == c2
