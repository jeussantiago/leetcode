class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        '''
        Time: O(nlogn)
            ; (nlogn) python sorting
            ; (n) iterrating over all of array
        Space: O(n)
            ; (n) python sorting
        '''
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False

        return True
