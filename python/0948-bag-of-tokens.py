class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        '''
        two pointers

        - sort
        - the lowest power scores: we want to use them to get a point using the
        least amount of power needed
        - the highest power scores: we ant to use them to get the most amounts
        of points possible for the least the one score point

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) two pointer traversal
        Space: O(n)
            ; (n) sorting
            ; (1) two pointer traversal
        '''

        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        while left <= right:
            if power >= tokens[left]:
                # can only get a score, if there is power to trade
                power -= tokens[left]
                score += 1
                left += 1

            elif left < right and score > 0:
                # can only add to power, if there is a score to trade
                power += tokens[right]
                score -= 1
                right -= 1

            else:
                # cant trade power or score
                return score

        return score
