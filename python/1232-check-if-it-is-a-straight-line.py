class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''
        Time: O(n)
        Space: O(1)
        '''

        def calculateSlope(coord1, coord2):
            x1, y1 = coord1
            x2, y2 = coord2
            if (x2 - x1) == 0:
                return float('inf')

            return (y2 - y1) / (x2 - x1)

        slope = calculateSlope(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            current_slope = calculateSlope(coordinates[i-1], coordinates[i])
            if current_slope != slope:
                return False

        return True
