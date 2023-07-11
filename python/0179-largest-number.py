class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        - mergesort
        - to compare 2 numbers to see which is bigger than the other
            - created 2 different string number of combination n1 + n2 and n2 + n1
            whichever is bigger, you grab the first number

        Time: O(nlogn)
        Space: O(n)
        '''
        # case of if 0 is the only number in the nums arr
        if all(num == 0 for num in nums):
            return "0"

        nums = [str(num) for num in nums]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return "".join(nums)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        sortedArr = self.mergeSort(nums)
        res = "".join(sortedArr)
        return res

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        l, r = 0, len(nums)-1
        mid = (l + r) // 2

        leftArr = self.mergeSort(nums[:mid+1])
        rightArr = self.mergeSort(nums[mid+1:])

        sortedArr = self.order(leftArr, rightArr)
        return sortedArr

    def order(self, arr1, arr2):
        sortedArr = []
        a1, a2 = 0, 0
        while a1 < len(arr1) and a2 < len(arr2):
            order1 = arr1[a1] + arr2[a2]
            order2 = arr2[a2] + arr1[a1]
            if order1 >= order2:
                sortedArr.append(arr1[a1])
                a1 += 1
            else:
                sortedArr.append(arr2[a2])
                a2 += 1

        if a1 < len(arr1):
            sortedArr += arr1[a1:]
        elif a2 < len(arr2):
            sortedArr += arr2[a2:]

        return sortedArr
