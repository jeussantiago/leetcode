class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        '''
        - if the current number hasn't been seen before, then we can add it to
        the first row in the 2D array
        - if the current number has been seen,
            - we can get the last position (row) of the number inserted from a hashmap
            - then add the number to the row afterwards

        Time: O(n)
        Space: O(n)
            ; (n) 2d array space will be the same size as 1d array
            ; (n) hashmap will contain that most n values
        '''
        last_row = {}
        two_d = [[]]
        for num in nums:
            if num not in last_row:
                two_d[0].append(num)
                last_row[num] = 0
            else:
                next_row = last_row[num] + 1
                if next_row >= len(two_d):
                    two_d.append([])

                two_d[next_row].append(num)
                last_row[num] += 1

        return two_d
