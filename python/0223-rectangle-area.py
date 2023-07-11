class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        '''
        - calculate area of a
        - calculate area of b
        - calculate area of overlap
            - left: max(ax1, bx1) - max of left of both rectangles
            - right: min(ax2, bx2)
            - top: min(ay2, by2)
            - bottom: max(ay1, by1)

            - (right - left) * (top - bottom)

        - total area = areaA + areaB - overlap

        Time: O(1)
        Space: O(1)
        '''

        # calculate area of A
        areaA = (ay2 - ay1) * (ax2 - ax1)

        # calculate area of B
        areaB = (by2 - by1) * (bx2 - bx1)

        # calculate area of Overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        x_overlap, y_overlap = (right - left), (top - bottom)

        # the rectangles won't always overlap
        # check if they are overlapping
        areaOverlap = 0
        if x_overlap > 0 and y_overlap > 0:
            areaOverlap = x_overlap * y_overlap

        return areaA + areaB - areaOverlap
