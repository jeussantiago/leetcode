class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        n = 5
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        - use rowIndex space
        - keep doing operation until lenght of array is same as rowIndex
        - if current indx is 0:
            - append 1 at the end of the list
        - elif ind is n:'
            - append 1 at the end of the list
            - remove beginnning of lsit
        - else
            - take value of indx + indx-1 and append to end of list
            - remove beginning of list


        Time: O()
        Space: O(n)
        '''

        output = [1]
        current_row = 1

        while current_row <= rowIndex:
            for n in range(current_row+1):
                if n == 0:
                    output.append(1)
                elif n == current_row:
                    output.append(1)
                    output.pop(0)
                else:
                    value = output[0] + output[1]
                    output.append(value)
                    output.pop(0)

            current_row += 1

        return output
