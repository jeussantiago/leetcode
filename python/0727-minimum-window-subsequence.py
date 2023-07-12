class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        '''
        s1 = "abdbebdecae", s2 = "bdcae"

        Time: O(n * m)
        Space: O(n + m) ; indices dict + dp
             : O(n)
        '''
        n = len(s1)
        m = len(s2)
        res = ""
        indices = collections.defaultdict(list)
        for i in range(n):
            indices[s1[i]].append(i)
        dp = [0] * m

        for start in range(n):
            prev_letter_ind = start - 1
            for j in range(m):
                # if the char in s2 doesn't exist in s1, theres no way to even create s2
                if s2[j] not in indices:
                    return ""

                # referencing from the current index recorded in the dp of the last time the char appeared in the substring
                # go to next index if teh current value of index is less than the previous
                # "ab" ; {a: [1,5], b: {2,6}}
                # if index 1 of the last for "a" is recorded in the dp, then that corresponds to index 5 of s1
                # index 0 is recorded for "b". the index value of b at 0 2 which is less than the previous letter which is "a" at index 5 of s1
                # so go to next index until the value is > 5/last previous letter index
                cur_indices = indices[s2[j]]
                while dp[j] < len(cur_indices) and cur_indices[dp[j]] <= prev_letter_ind:
                    dp[j] += 1

                # if the current letter index goes out of bounds, this means that we won't find any more
                # letter indecies/remaining letters in the rest of the substring to complete s2
                # just return what we have calculated so far
                if dp[j] == len(cur_indices):
                    return res

                prev_letter_ind = cur_indices[dp[j]]

            if res == "" or prev_letter_ind - start + 1 < len(res):
                res = s1[start:prev_letter_ind+1]

        return res
