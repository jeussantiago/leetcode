class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Solution 1:
        rearange each str so that they are alphabetical in order : tan -> ate
        - since they're anagrams they'll all equal the same
        - this way we can know which words match
        Time: O(m*nlogn) where m is the length of strs and n is the length of the individual str

        Solution 2:
        Get the unicode for each letter
        - every letter has a specific number so we can just add those to a counter
        - store the total unicode value as a key
        - collect the words with the same unicode value

        Time: O(m*n) where m is the length of strs and n is the length of each str
        '''
        #Solution 2
        res = collections.defaultdict(list)
        for s in strs:
            unicode_value = [0] * 26
            for c in s:
                unicode_value[ord(c) - ord('a')] += 1
            #[2,0,1,0,0] => caa (shortened version of 26 letters)
            res[tuple(unicode_value)].append(s)
        return [val for val in res.values()]
        