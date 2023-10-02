class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        '''
        "AAAABBBAABBB"
        - even if you remove the "B" from index 4, the other B's and the A's seperating the B's on the
        would never meet because you wouldn't be able to remove them since they don't meet the
        requirements of colors[i-1] == colors[i] == colors[i+1]
        - the furthest you could reduce something like this, following the requirements is:
            "AABBAABB"
        - as you can see, you can reduce it any further

        Solution:
        - count the number of potential moves each person can make
            - don't need to play optimally, just need to make more moves

        - if the counts are the same, that means that alice can't make a move so Bob wins

        Time: O(n)
        Space: (1)
        '''

        aliceMoves = bobMoves = 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == "A":
                    aliceMoves += 1
                else:
                    bobMoves += 1

        if bobMoves >= aliceMoves:
            # Bob wins
            return False
        # Alice wins
        return True
