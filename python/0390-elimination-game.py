class Solution:
    def lastRemaining(self, n: int) -> int:
        '''
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        - head goes to 2
        - remove half of the arr
            - mimicking removing [1,3,5,7,9]
        - increase the step to 2
        [2,4,6,8]
        - this iteration goes from right to left now so we don't increase the head, but we do delete half of the arr and increase the step
        - remove half of the array
            - mimick removing [8,4]
        - increase step to 4

        [2,6]
        - left to right now
            - head gets moved up by the number of steps which is 4
            - head is 6 now
        - delete half of the array
            - mimick removing [2]
        - increase the step to 8

        Time: O(logn)
        Space: O(1)
        '''

        head, remain = 1, n
        left_to_right = True
        step = 1
        while remain > 1:
            if left_to_right or remain % 2 == 1:
                head += step

            remain //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
