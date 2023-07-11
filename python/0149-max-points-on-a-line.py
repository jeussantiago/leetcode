class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        - lines can have slopes that are greater or less than +/- 1
        - if multiple points between them have the same slope, it is going to be on the same line
        - multiple points can have the same slope but not be on the same line
            - to get around this, we have a slope hashmap initialized after every position

        go thorugh every position
            - create a slope hashmap
            - go through every position after the current position
                - calculate slope
                - hashmap[slope] += 1

                - get the max points on a line


        Time: O(n^2)
        Space: O(n)
        '''
        # start at 1 cause there is going to be atleast 1 point in the points array
        output = 1
        N = len(points)
        for i in range(N):
            line = collections.defaultdict(int)
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                line[slope] += 1
                # +1 because you need to account for the (x1, y1) point
                # but you only account for it 1 time, not all the time
                output = max(output, line[slope] + 1)

        return output
