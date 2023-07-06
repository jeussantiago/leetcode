class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        1) there has to be atleast 1 string in array
        2) string can be empty
        3) strings only contian lowercase letters
        [flowing, flow]
        Time: O(nm) where n is the total number of words given and m is the min size of a string
        '''
        shortest_word = len(min(strs, key=len))
        i = 0
        common_prefix = ""

        while i < shortest_word:
            current_prefix = strs[0][:i+1]
            for word in strs:
                if word[:i+1] != current_prefix:
                    return common_prefix
            i += 1
            common_prefix = current_prefix
        
        return common_prefix
