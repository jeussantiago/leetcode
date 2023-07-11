class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        insert
            - the substring withouth the character at the current index of t
            (removed the character at t)
            s == t[:i] + t[i + 1:]

        delete
            - same as insert but this time for s
            s[:i] + s[i + 1:] == t

        replace
            - don't include the current index at both s and t
            s[:i] + s[i + 1:] == [:i] + t[i + 1:]

        - we don't need to include the trailing characters, since we've already looked at them

        '''
        len_s, len_t = len(s), len(t)
        if (
            abs(len_s - len_t) > 1 or
            s == t
        ):
            return False

        def insertStrng(i):
            return s[i:] == t[i + 1:]

        def deleteStrng(i):
            return s[i + 1:] == t[i:]

        def replaceStrng(i):
            return s[i + 1:] == t[i + 1:]

        for i in range(min(len_s, len_t)):
            if s[i] != t[i]:
                return (
                    insertStrng(i) or
                    deleteStrng(i) or
                    replaceStrng(i)
                )

        return True


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        go through the indexes of the bigger string

        insert
            s[:i] + t[i] + s[i:]

        delete
            s[:i] + s[i + 1:]

        replace
            s[:i] + t[i] + s[i + 1:]


        Time: O(max(n, m)) where n is the len of s and m is the len of t
        Space: O(1)
        '''
        S, T = len(s), len(t)
        if not s and not t:
            return False
        if s == t:
            return False  # 0 distances apart
        if T > S + 1 or T < S - 1:
            return False

        def insertStrng(i):
            if i >= len(t):
                return False
            new_s = s[:i] + t[i] + s[i:]
            return new_s == t

        def deleteStrng(i):
            if i >= len(s):
                return False
            new_s = s[:i] + s[i + 1:]
            return new_s == t

        def replaceStrng(i):
            if i >= len(s) or i >= len(t):
                return False
            new_s = s[:i] + t[i] + s[i + 1:]
            return new_s == t

        for i in range(max(S, T)):
            if insertStrng(i):
                return True
            if deleteStrng(i):
                return True
            if replaceStrng(i):
                return True

        return False
