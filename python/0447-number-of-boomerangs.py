class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        '''
        Time: O(n^2)
        Space: O(n)
        '''
        res = 0
        for x1, y1 in points:
            counter = collections.defaultdict(int)
            for x2, y2 in points:
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if dist in counter:
                    res += 2 * counter[dist]

                counter[dist] += 1

        return res
