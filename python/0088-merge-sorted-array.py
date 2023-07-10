class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        work backwards:
        - m tells us the amount of elements in num1 but also the index where the elements finish showing up in the array
            (elements after this index is to fill with numbers from num2)
        - n tells us the amount of elements in num2
        - originally had the idea of inserting and popping elements and 0 values
        - what we can do is work backwards
        - 3 pointers,(indexes)
            - m-1
            - n-1
            - len(nums1)-1
        - if a number is greater than the other, place it in the location of the third pointer
            - whichever was greater, -= its pointer
            - -= third pointer


        if N is negative, the rest of the space is already in order naturally
        if M is negative, the rest of the space needs to be filled with nums2

        Time: O(m + n)
        Space: O(1)
        """

        if n == 0:
            return nums1

        M, N, i = m-1, n-1, m+n-1

        while M >= 0 and N >= 0:
            if nums1[M] >= nums2[N]:
                nums1[i] = nums1[M]
                M -= 1
            else:
                nums1[i] = nums2[N]
                N -= 1
            i -= 1

        if M < 0:
            # the rest of the space should be filled with nums2
            nums1[:i+1] = nums2[:N+1]
