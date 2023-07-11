class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        Divide and Conquer

        - get a counter for current string
        - check at every position in the string if the counter for the char is < k
            - if < k
                - split the string in half to imitate removing the current char
                Ex: 
                s = ababcabbaa ; k = 2
                - c in the counter is 1, which is < k
                - explore two different paths (divide and conquere), the left side of the current char and the right side
                dfs(s=abab), dfs(s=abbaa)

        - we return imediately once we find a count < k
        b/c if this char is < k, that means the same char is < k later in the string
        so theres no reason to keep this char, best to just get rid of it immediately

        Time: O(n^2)
        Space: O(n) ; recursion call stack
        '''
        def dfs(strng):
            count = collections.Counter(strng)
            for i, char in enumerate(strng):
                if count[char] < k:
                    # left side, right side
                    return max(dfs(strng[:i]), dfs(strng[i+1:]))
            return len(strng)

        return dfs(s)
