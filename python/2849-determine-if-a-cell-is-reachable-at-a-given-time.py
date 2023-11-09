class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        '''
        Method 1:
        - simulate gettting to the finish position
        - you can go diagonal so go diagonal until you reach the height of
        the finish position, then just traverse left or right until you get
        to the finish position

        - if you run out of time then return False

        W is the difference in width between start and finish position
        H is the difference in height between start and finish position
        Time: O(max(W, H))
        Space: O(1)

        Method 2: (Implemented here)
        - you don't need to simulate since you can calculate the distance
        you need to travel
            - since you can go diagonal, we can go directly to the finish
            and not worry about going strictly vertical or horizontal

        - the travel time depends the max distance of the difference in height
        or width

        Time: O(1)
        Space: O(1)
        '''

        width = abs(sx - fx)
        height = abs(sy - fy)
        # case of start and finish on top of each other
        if width == 0 and height == 0 and t == 1:
            return False
        return t >= max(width, height)
