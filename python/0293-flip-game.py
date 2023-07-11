class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        res = []
        i = 0
        while i < len(currentState) - 1:
            sub = currentState[i: i + 2]
            if sub == "++":
                res.append(currentState[:i] + "--" + currentState[i + 2:])
            i += 1
        return res
