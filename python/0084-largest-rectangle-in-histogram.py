class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Stacks:
        - add height and index to stack
        - if the previous heights/ already in stack are bigger than the current height
            - compute the area that it could have created
            - pop that height
            - update the starting index of the current height to the starting index of the item that just popped
            [2,1]
            stack
            ------
            index, height
            0, 2 -> pop
            1, 1 -> 0, 1 (updated index b/c previous height is taller)

            - if the next hight is bigger than the current height, then we can just add to stack
            - we don't pop the 1 because it can still be extended horizontally
            - same concept with just adding the increasing heights, b/c they can also be extended horizontally
            - just update the indexes when you reverse
            stack 
            -------
            index, height
            0, 1 -> 0, 1
            2, 5 -> pop (max height = 10)
            3, 6 -> pop (max height = 6)
            4, 2 -> 2, 2

            - now there is a decreasing number; do operation 
                - check if the number in stack/previous heights are bigger than current height
                - figure out the max height it could have created
                - update current height with new index

            - contents of final stack are numbers that can be extended to the very end of the histogram
            - final stack looks like this:
            --------------------------
            index, height
            0, 1 -> max= 6-0 * 1 = 6
            2, 2 -> max= 6-2 * 2 = 8
            5, 3 -> max= len(heights)-5 * 3 = 1 * 3 = 3

            now just get the max possible heights for each

        Time: O(n) push elements onto our stack once but pop it once also
        Space: O(n) size of stack is the size of the heights array
        '''

        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            height_start_index = i
            while stack and stack[-1][1] > h:
                j, height = stack.pop()
                maxArea = max(maxArea, (i - j) * height)
                height_start_index = j

            stack.append((height_start_index, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
