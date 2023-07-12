class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        - similar to an interval problem

        - sort by the starting index

        if start of current range <= end of the previous range
            - they intersect
            - we need to update the current range to be the intersection of the two
            new_range = [start_of_curr, end_of_last]

        elif start of current range > end of the previous range
            - don't intersect
            - need another dart (increase dart count + 1)
            - update the previous range to be the current range 

        Ex: [[1,2],[2,3],[3,4],[4,5]]
        [-inf, -inf] [1,2]
        darts = 1 ; [1,2]
        [1,2] [2,3]
        - darts doesn't increase since they intersect, new range is the intersection of the two
        darts =1 ; [2,2]
        [2,2] [3,4]
        - don't intersect so increase dart count; new range becomes the curent range
        darts=2 ; [3,4]
        [3,4] [4,5]
        - intersect
        darts=3 ; [4,4]

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) iterating through array
        Space: O(n)
            ; (n) python sorting
            ; (1) darts var and intersection arr
        '''

        points = sorted(points, key=lambda x: x[0])

        darts = 0
        intersect = [float('-inf'), float('-inf')]
        for start, end in points:
            if start <= intersect[1]:
                intersect = [start, min(intersect[1], end)]
            else:
                intersect = [start, end]
                darts += 1

        return darts
