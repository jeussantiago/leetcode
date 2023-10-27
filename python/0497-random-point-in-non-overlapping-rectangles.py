class Solution:
    '''
    store the rectangles

    - create uniform probability using the rectangle area

    - when you random pick
        1. pick random rectangle
        2. pick random range for x in the rectangle
        3. pick random range for y in the rectangle

    n is the number of rectangles they give
    Time: O(1)
    Space: O(n)
    '''

    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.areas = []
        for (x1, y1, x2, y2) in self.rectangles:
            area = (y2 - y1 + 1) * (x2 - x1 + 1)
            self.areas.append(area)

    def pick(self) -> List[int]:
        # can't use 'choice' since it doesnt have a weight parameter. have to use 'choices'
        rec = random.choices(self.rectangles, weights=self.areas, k=1)[0]
        x = random.randint(rec[0], rec[2])
        y = random.randint(rec[1], rec[3])
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
