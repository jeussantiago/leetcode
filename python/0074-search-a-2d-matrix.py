class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Solution 2:
        - treat this 2d array like a 1d array - do binary search on the position in array
            - find someway to keep track of the row/col you're on
            - floor(//) by the cols can give us the rows
            - mod(%) by the cols can give us the cols
        
        Time: O(log m+n)
        Space: O(1)
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, (ROWS*COLS)-1

        while low <= high:
            mid = (low + high) // 2
            mid_value = matrix[mid//COLS][mid%COLS]

            if target == mid_value:
                return True
            elif target < mid_value:
                high = mid - 1
            else:
                low = mid + 1
        return False
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        binary search on 2d array
        - binary serach on col
        - binary serach on row

        Time: O(log m + log n) search the col + search the row
        Space: O(1)
        '''

        #target doesn't exist in the range
        if target not in range(matrix[0][0], matrix[-1][-1]+1): return False
        #we know target exist within the range so target_row will never be -1
        target_row = -1
        low, high = 0, len(matrix)-1
        # get the target row
        while low <= high:
            mid = (low + high) // 2
            if target in range(matrix[mid][0], matrix[mid][-1]+1):
                target_row = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        #check if target in row
        low, high = 0, len(matrix[0])-1
        while low <= high:
            mid = (low + high) // 2
            mid_value = matrix[target_row][mid]
            if target == mid_value:
                return True
            elif target < mid_value:
                high = mid -1
            else:
                low = mid + 1

        #target doesn't exist
        return False
