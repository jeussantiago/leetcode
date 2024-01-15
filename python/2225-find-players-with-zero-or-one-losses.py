class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        losses = collections.defaultdict(int)
        for winner, loser in matches:
            losses[loser] += 1
            # dont change the count of losses of the winner, but if
            # the winner only shows up once, we we need to record it
            # in the keys, so give a value of 0
            losses[winner] = losses.get(winner, 0)
        no_lose, one_lose = [], []
        for num, cnt in losses.items():
            if cnt == 0:
                no_lose.append(num)
            elif cnt == 1:
                one_lose.append(num)

        return [sorted(no_lose), sorted(one_lose)]
