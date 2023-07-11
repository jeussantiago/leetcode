class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        '''
        - value of a decides whether parabola is upward facing or downwward facing
            - positive 'a' means upward facing
            - negative 'a' means downward facing

        - if a is positive
            - parabola is upward facing
            - the ends of the sorted array_x will be the ends of the parabola
            - this means the we can store whichever is GREATER THAN and move that pointer
            [193,190,5,2]
            - reverse this
        - if a is negative
            - parabola is downward facing
            - the ends of the sorted array_x will be the ends of the parabola
            - this means the we can store whichever is LESS THAN and move that pointer
            [-190,-50,-3,5,7]

        Time: O(n)
        Space: O(n)
        '''

        def calculate(num):
            return (a * (num**2)) + (b * num) + c

        res = []
        l, r = 0, len(nums)-1
        if a >= 0:
            # upward facing parabola
            while l <= r:
                left = calculate(nums[l])
                right = calculate(nums[r])
                if left >= right:
                    res.append(left)
                    l += 1
                else:
                    res.append(right)
                    r -= 1
            res.reverse()

        else:
            # downward facing parabola
            while l <= r:
                left = calculate(nums[l])
                right = calculate(nums[r])
                if left <= right:
                    res.append(left)
                    l += 1
                else:
                    res.append(right)
                    r -= 1

        return res
