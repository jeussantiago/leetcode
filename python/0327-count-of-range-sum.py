from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        [13, 6,  13,  4, 27,-14,-13, 15, -4, 13] ; lower=25 ; upper=37
        [13, 19, 32, 36, 63, 49, 36, 51, 47, 60]

        [0] 
        13 - lower = 13 - 25 = -12
        13 - upper = 13 - 37 = -24
        - we would put both to the left of 0
        - add curr_total
        [0,13]
        19 - lower = -6
        19 - upper = -18
        - put both to the left of 0
        [0, 13, 19]
        - lower diff = 7 ; insert at index 1
        - upper diff = -5 ; insert at index 0
        - lower_diff insertion - upper_diff insert = 1 - 0
        (there is 1 subarray that is between the range)
        [0, 13, 19, 32]
        - lower diff = 11 ; insert at index 1
        - upper diff = -1 ; insert at index 0
        - lower_diff insertion - upper_diff insert = 1
        (there is 1 subarrays that are between the range)

        - the lower difference will tell us the upper boundary in the prefix sorted arr
        - the upper difference will tell us the lower boundary in the prefix sorted arr
        - the lower will generally be gettinga  bigger index which is why we have it in from
        - the since each boundary tells us where it would be, in the array, then the difference is how many subarrays will appear
        between the 2 lower and upper ends

        Time: O(n * (logn + logn)) iterating through entire nums ;  
                    adding to the sortedList is like adding to a heap O(logn) ;
                    searching where to insert the lower and upper boundaries is O(logn) since it uses bisect/binary search
                    (we can use binary serach since its sorted)
            : O(n * (2logn))
            : O(n2logn))
            : O(nlogn)
        Space: O(n)

        '''
        sorted_nums = SortedList()
        sorted_nums.add(0)
        total, res = 0, 0
        for num in nums:
            total += num
            res += sorted_nums.bisect_right(total - lower) - \
                sorted_nums.bisect_left(total - upper)
            sorted_nums.add(total)

        return res
