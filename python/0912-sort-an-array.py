class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        bubble sort
        Time: O(n^2)
        Space: O(1)
        '''

        # for i in range(len(nums)):
        #     for j in range(0, len(nums)-1-i):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # return nums

        '''
        quicksort
        Time: worst O(n^2) ; average O(nlogn)
        Space: O(logn)
        '''
        # # all values less than pivot go to the left
        # # all values greater than the pivot go to the right
        # def partition(lst, low, high):
        #     pivot = lst[high]

        #     # pointer for values greater than pivot
        #     i = low-1

        #     # leave the values greater than pivot alone
        #     # if the value is less than pivot, swap the position with the greater than pointer
        #     for j in range(low, high):
        #         if lst[j] <= pivot:
        #             i += 1
        #             lst[i], lst[j] = lst[j], lst[i]
        #     # swap the pivot with the position after the values less than itself
        #     lst[i + 1], lst[high] = lst[high], lst[i + 1]

        #     # return the pivot position
        #     return i + 1

        # def quicksort(lst, low, high):
        #     if low < high:
        #         pivot = partition(lst, low, high)

        #         quicksort(lst, low, pivot-1)
        #         quicksort(lst, pivot+1, high)

        # quicksort(nums, 0, len(nums)-1)
        # return nums

        '''
        Mergesort
        Time: O(nlogn)
        Space: O(n)
        '''

        def merge(leftLst, rightLst):
            res = []
            left_index, right_index = 0, 0
            while left_index < len(leftLst) and right_index < len(rightLst):
                if leftLst[left_index] < rightLst[right_index]:
                    res.append(leftLst[left_index])
                    left_index += 1
                else:
                    res.append(rightLst[right_index])
                    right_index += 1

            # extend is faster than +=
            res.extend(leftLst[left_index:])
            res.extend(rightLst[right_index:])
            return res

        def mergeSort(lst):
            if len(lst) <= 1:
                return lst

            # divide and conquer
            half = len(lst) // 2
            leftLst = mergeSort(lst[:half])
            rightLst = mergeSort(lst[half:])

            # merge the two halfs together
            return merge(leftLst, rightLst)

        res = mergeSort(nums)
        return res
