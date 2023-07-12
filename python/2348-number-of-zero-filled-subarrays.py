class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        [0]
        1 occurrence of [0]
        total = 1

        [0,0]
        2 occurrences of [0]
        1 occurrence of [0,0]
        total = 3

        [0,0,0]
        3 occurrences of [0]
        2 occurrence of [0,0]
        1 occurrence of [0,0,0]
        total = 6

        [0,0,0,0]
        4 occurrences of [0]
        3 occurrence of [0,0]
        2 occurrence of [0,0,0]
        1 occurrence of [0,0,0,0]
        total = 10

        - at each new 0, there is an extra subset of each level from the previous level + the current level
        Ex:
            [0,0,0,0] ; n = 4
            - there is an extra set of [0]
            - there is an extra set of [0,0]
            - there is an extra set of [0,0,0]
            - there is a new set of [0,0,0,0]

        - this is the same for every new 0 added
        - so just take the previous total and add the current length


        Implementation:
        - zero_counter
            - if current number == 0:
                zero_subarray_size +=

                - keep track of the running subarray total
                subarray_total += zero_subarray_size

            else current number != 0:
                zero_subarray_size = 0

        Time: O(n)
        Space: O(1)
        '''
        zero_subarray_size = 0
        subarray_total = 0
        for num in nums:
            if num == 0:
                zero_subarray_size += 1
                subarray_total += zero_subarray_size
            else:
                zero_subarray_size = 0
        return subarray_total
