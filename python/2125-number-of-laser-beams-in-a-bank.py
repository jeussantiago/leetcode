class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        '''
        Time: O(m * n)
        Space: O(1)
        '''

        lasers = 0
        prev = cnt = 0
        for row in bank:
            for cell in row:
                if cell == '1':
                    cnt += 1

            if cnt > 0:
                lasers += (prev * cnt)
                prev = cnt
                cnt = 0

        return lasers
