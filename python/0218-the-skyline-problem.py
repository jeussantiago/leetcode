import sortedcontainers


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        - keep track of the active heights
        - python has a sortedList

        Time: O(nlogn)
        Space: O(2n) => O(n)

        '''
        # buildings = [[2,9,10],[2,7,15],[5,12,12],[15,20,10],[19,24,8]]

        points = []
        for l, r, h in buildings:
            points.append((l, h, 1))  # building going up
            points.append((r, h, -1))  # building going down

        points.sort(key=lambda x: (x[0]))

        res = []
        active_heights = sortedcontainers.SortedList([0])
        n = len(points)
        i = 0
        while i < n:
            x_pos = points[i][0]  # x-pos
            while i < n and x_pos == points[i][0]:
                # print(points[i])
                _, y_pos, t = points[i]

                if t == 1:
                    active_heights.add(y_pos)
                else:
                    active_heights.remove(y_pos)

                i += 1

            # make sure its not the same height
            if not res or res[-1][1] != active_heights[-1]:
                res.append((x_pos, active_heights[-1]))

        return res
