class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Time: O(n^2)
        # Space: O(1)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if (
                    j >= len(words) or
                    i >= len(words[j]) or
                    words[i][j] != words[j][i]
                ):
                    return False
        return True
