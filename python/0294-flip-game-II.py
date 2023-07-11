class Solution:
    def canWin(self, currentState: str) -> bool:
        '''
        - you go first
        1 - lost
        2,3,4 - winnable
        "+--+"
        5 - lost
        6 - lost
        7 - winnable
        res = opposite of what will happen in the previous n-1 or n -2
        8 - winnable
        "++++++"

        "++++-++++"
        hashmap
        key=size of n wehre is the length of the + subarray
        val= True if winnable and False if not winnable

        {
            "" : lost
            1: lost 
            2: win
            3: win
        }

        Time: O(n^2)
        Space: O(n)
        '''
        # currentState = "++++-++++-++++"

        memo = dict()

        def dfs(s):
            if s in memo:
                return memo[s]

            for i in range(len(s)-1):
                if s[i: i + 2] == "++":
                    new_s = s[:i] + "--" + s[i + 2:]
                    if not dfs(new_s):
                        memo[s] = True
                        return True

            memo[s] = False
            return False

        return dfs(currentState)
