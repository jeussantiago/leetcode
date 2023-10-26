class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        mergesort variation

        - do merge sort
        - when you put the numbers back together, in the comparison portion, you can test
        if one number is > 2x the other number
            - if true, then you can increase the count, and since its sorted, you can 
            take the remaining length since everything is going to greather than the 2x

        Time: O(nlogn)
        Space: O(n)
        '''

        def mergesort(nums, low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2
            # split
            pair_count = mergesort(nums, low, mid) + \
                mergesort(nums, mid + 1, high)

            # merge
            # get the count of reverse pairs
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                pair_count += j - (mid + 1)

            # do normal merge sort/ sort the values from the low to high range
            nums[low: high + 1] = sorted(nums[low: high + 1])

            return pair_count

        return mergesort(nums, 0, len(nums) - 1)
