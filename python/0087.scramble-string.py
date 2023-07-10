class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        '''
        s1 = "great", s2 = "rgeat"

        - need to find a way to optimize
            - don't want to do repeated work
            - can do memoization


        - at any given index, we want to compare the substrings,
            - if the substrings == each other, then we don't want to continue down 
            the same line and split it up, just stop there for that side

        - theres two cases to this problem
        - at either left or ride half, each can be swapped or not swapped

        s1 = "great", s2 = "rgeat"
        i = 2
        left half //// right half
        s1[:2] = "gr" ; s2[:2] = "rg" //// s1[2:] = "eat" ; s2[2:] = "eat"
        - left half doesn't equal each other, so we need to SWAP it
        - right half equals each other, so we DON'T SWAP

        - if the lengths of the strings become uneven, then just return False

        - - to optimize, we can process the swapping
        s1 = 'abc' , s2 = 'bca'

        - we need to compare the first half of s1 with the second half of s2, vice versa
        s1[:1] = 'a' , s2[-1:] = 'a  ; s1[1:] = 'bc' , s2[:-1] = 'bc'
            - now just compare these

        Don't Swap:
        - compare front of s1, with front of s2
        - compare back of s1, with back of s2

        Swap:
        - compare front of s1, with back of s2
        - compare back of s1, with front of s2

        '''

        if len(s1) != len(s2):
            return False

        m = dict()

        def dfs(string1, string2):
            if (string1, string2) in m:
                return m[(string1, string2)]

            if string1 == string2:
                m[(string1, string2)] = True
                return True

            if len(string1) != len(string2):
                m[(string1, string2)] = False
                return False

            for i in range(1, len(string1)):
                # not swapping - comparing substrings from the front
                if dfs(string1[:i], string2[:i]) and dfs(string1[i:], string2[i:]):
                    m[(string1, string2)] = True
                    return True

                # swapping - comparing the front of s1 to the back of s2 and vice versa
                if dfs(string1[:i], string2[-i:]) and dfs(string1[i:], string2[:-i]):
                    m[(string1, string2)] = True
                    return True

            m[(string1, string2)] = False
            return False

        res = dfs(s1, s2)
        return res
