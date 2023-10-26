class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        '''
        brute force
        work backwards - first to find is the solution

        n is the value of area
        Time: O(n)
        Space: O(1)
        '''
        for num in range(int(sqrt(area)), 0, -1):
            if area % num == 0:
                return [area // num, num]
