class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        '''
        Time: O(nlogn)
        Space: O(n)
            ; (n) python sorting takes up n space
        '''
        arr.sort()
        arr[0] = 1
        curr_num = 2
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] <= 1:
                curr_num = arr[i] + 1
            else:
                arr[i] = curr_num
                curr_num += 1

        return arr[-1]


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        '''
        [2,2,1,2,1,3,7,5]
        [0,2,3,1,0,1,0,1,0] = count of how many times a num appears - if the num exceeds N, then just add to the length of the array
        - no number will exceed the length of array
        [  1,2,3,3,4,4,5,5]

        Time: O(n)
        Space: O(n)
        '''
        n = len(arr)
        counts = [0] * (n + 1)

        for num in arr:
            counts[min(num, n)] += 1

        ans = 1
        for num in range(2, n + 1):
            ans = min(ans + counts[num], num)

        return ans
