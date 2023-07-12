class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        '''
        - treat the index as the peak value
            - everything to the left decreases by 1
            - everything to the right decreases by 1

            - at some point, wehn the value reaches 1, just put 1 is those places
            EX: [2,3,2,1,1,1,1,1] if index=1

        - binary search to find the mid point of the max value of the peak
            - value to compare in the binary search is the sum of the array given a peak value/mid value

        LEFT SIDE:

        if value > index
        [1,2,3] and [3,4,5]
            - sum formula = (peak_val + peak_val - peak_val_indx) * (peak_val_indx + 1) // 2

        else value <= index
        [1,1,2]
            - (peak_val + 1) * peak_val // 2 + peak_val_indx - peak_val + 1

        Right Side:
            - similar idea but index gets modified since there could be more or less: (n - peak_val_ind)

        - in both cases, we added the peak_val so we need to remove that from the final sum

        Binary Search:
            - if sum <= maxSum:
                l = mid : mid is part of the solution set so we dont want to ignore it
            else
                r = mid - 1

        Time: O(logn(maxSum))
        Space: O(1)
        '''

        def getSum(index, value, n):
            total = 0
            # Left Side of peak
            if value > index:
                total += (value + value - index) * (index + 1) // 2
            else:
                total += ((value + 1) * value // 2) + index - value + 1

            # Right side of peak
            if value >= n - index:
                total += (value + value - (n - index - 1)) * (n - index) // 2
            else:
                total += (value + 1) * value // 2 + (n - index) - value

            # value was used in both sides of the calculations so we need to remove one of them
            return total - value

        l, r = 1, maxSum
        while l < r:
            mid = (l + r + 1) // 2
            if getSum(index, mid, n) <= maxSum:
                l = mid
            else:
                r = mid - 1

        return l
