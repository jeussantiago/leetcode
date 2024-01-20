class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ''' 
        Monotonic Stack

        Time: O(n)
        Space: O(n)
        '''
        MOD = 10 ** 9 + 7
        stack = []  # store indexes
        res = 0

        # do +1 to empty the stack at the end
        for i in range(len(arr) + 1):
            # empty the stack if reached the end of the array
            # OR remove item from stack if top of stack >= current number
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                # count the number of subarrays the element at mid position is the minimum number
                count = (mid - left) * (right - mid)
                res += (count * arr[mid])

            stack.append(i)

        return res % MOD
