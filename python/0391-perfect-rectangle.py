class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        '''
        - just need to check if the area that the rectangles take up == the area that is calculate from the lowest 
        bot-left and furthest top right

        Time: O(n)
                ; (n) to go through all the corners in the rectangle
                ; (1) since we know there are only 4 elements in the corners arr, we know exactly the number of processes to 
                ;   get the correct bot_left corners and top_right corner
        Space: O(n)
                ; each corner in the corners set can be taken up

        '''
        actual_area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            # keep track of the min bot_left positions as well as the max top_right positions
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

            # calculate the amount of area this rectangles takes up
            actual_area += (y2 - y1) * (x2 - x1)

        # get rid of case of chape of image not being a rectangle
        if len(corners) != 4:
            return False

        # get the bot_left and top_right of rectangle
        x1, y1 = float('inf'), float('inf')
        x2, y2 = float('-inf'), float('-inf')
        for x, y in corners:
            x1, y1 = min(x1, x), min(y1, y)
            x2, y2 = max(x2, x), max(y2, y)
        # calculate area of supposed rectangle
        calculated_area = (y2 - y1) * (x2 - x1)

        return calculated_area == actual_area
