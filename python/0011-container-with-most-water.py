class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        1) always atleast 2 elements in list
        2) value within element between 0 and 10^4

        1) left and right pointers - calculater area
        2) shift left or right pointer over if it is lower than the other (greater height leads to greater area) i.e. 1,...., 7 -> 8,...., 7
        3) it heights are equal, we can shift either one to the next (could also shift the one with a greater next height)

        Time: O(n)
        '''
        maxArea = 0
        l, r = 0, len(height) - 1
        #always going to be comparing two heights, can't comapre the heigh with itself, we know we are done at that point
        while l != r:
            distance = r - l
            area = distance * min(height[l], height[r])
            maxArea = max(maxArea, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

