class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        '''
        s    = "abgdefcp"
        goal = "abcdefgh"

        - count how many mismatches there are

        "aac"
        "aad"
        - this case only works if everything is the same character
            - otherwise, doesn't work and we have to go based on the mismatch count

        different approach if S and Goal are == and if theyre not:
        if ==
            "aac" and "aac" vs 'aaa' and 'aaa'
            - if there exista  character that is repeating >= 2
                - return true

        if !=
            - find the mismatches
            - once mismatches are found
                - if number of mismatches != 2
                    return False

            - compare the 2 mismatched letters



        Time: O(n)
        Space: O(1)
        '''
        if len(s) != len(goal):
            return False

        if s == goal:
            cnt = collections.Counter(s)
            for val in cnt.values():
                if val >= 2:
                    return True

        mismatched_pos = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatched_pos.append(i)

        if len(mismatched_pos) != 2:
            return False

        return (
            s[mismatched_pos[0]] == goal[mismatched_pos[1]] and
            s[mismatched_pos[1]] == goal[mismatched_pos[0]]
        )
