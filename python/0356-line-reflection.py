class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        '''
        x   x
        x   x
        True
        ----
        x   x
         x   
        False

        [(2,1), (0, -1)] ; mid=1

        - reflection of position
            => (2 * mid_symmetry_pos) - x

            Ex: 2 * 1 - 2 = 2 - 2 = 0

        - check if reflection coordinates exist

        n is the len of points
        Time: O(2n) ; (n) get rid of duplicates
                  ; (n) check if the points reflection is in the coords 
            : O(n)
        Space: O(n) set
        '''
        # get rid of duplicates and get the symmetrical x position
        mid = 0
        coords = set()
        for x, y in points:
            coords.add((x, y))

        for x, _ in coords:
            mid += x
        mid /= len(coords)
        for x, y in coords:

            # get the reflection
            x_reflec = (2 * mid) - x
            y_reflec = y
            # check if the reflection position exist
            if (x_reflec, y_reflec) not in coords:
                return False

        return True
