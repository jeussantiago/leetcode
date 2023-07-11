class Solution:
    '''
    prerequisite question: 1673. Find the Most Competitive Subsequence

    - we want to find the lexicographical order of arrays at k length
    - we want the biggest numbers to be first in the array and the min at the end

    [3,4,6,5] and [9,1,2,5,8,3] and k=10
    if arr2_k = 10 or 9 or any number greater than it's lenght, then there no reason to keep processing this arry
    - skip all the k values where it is greater than the length
    (for this example it onyl works at arr1_k=4 and arr2_k=6)


    ** we don't know how many numbers we need from array 1 and how many from array 2
    ( Ex: nums1 = [3,4,6,5]
        if k=4 ; res=[3,4,6,5]
        if k=3 ; res=[3,4,5]
    )
    - so we can't avoid exploring all possibilities of the length up to K
    - do this for both arrays
    - if k = 5 ; arr1.len=4 ; arr2.len=1
    - if k = 5 ; arr1.len=3 ; arr2.len=2
    - total has to add up to k

    - merge the two arrays together
    - 2 pointers
    arr1=[2,1,1,0,2,0] ; arr2=[1,1,1,0,2,1]
    - 2 > 1
        - add 2 ; move arr1 pointer up
    res = [2]
    - 1 == 1
        - so we have to check which sequence of numbers is lexographically bigger(we do bigger cause question wants max) than the other
        - in the second position after the current pointer positions (arr1.pointer=1 + 2 => 0 ; arr2.pointer=0 + 2 => 1 )
            - this makes arr2 lexicographically bigger so we add that
            - move arr2 pointer up
    res = [2,1]
    - 1 == 1
        - repeat the process above
        - arr2 is bigger
    res = [2,1,1] ; arr1.pointer=1 ; arr2.pointer=2
    - 1 == 1
        - arr1 is bigger
    res = [2,1,1,1] ; arr1.pointer=2 ; arr2.pointer=2

    - if 1 array is longer than the other, but everything matches
        - we can give the benefit of the doubt that the longer one is the bigger sequence
        - or imagine that the shorter one has a bunch of 0's at the end 
        1010 and 10 => also see it as => 1010 and 1000 (but just take the longer sequence first)

    - in the end, save the sequence of numbers that is greatest
    [9, 8, 3, 4, 6] > [9, 5, 8, 4, 6] == 98,346 > 95,846

    Time: O(k * (n + m + (n + m))) ; loop up to k times, get lexicographical order for n and m ; merge the 2 arrays
        : O(k * (2n + 2m))
        : O(k * (n + m))
    Space: O(m + n)
    '''

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0]
        for nums1_k in range(k+1):
            nums2_k = k - nums1_k
            if nums1_k > len(nums1) or nums2_k > len(nums2):
                continue

            # print(nums1, nums1_k, nums2, nums2_k)
            nums1_lex = self.maxLexicographical(nums1, nums1_k)
            nums2_lex = self.maxLexicographical(nums2, nums2_k)
            merged_lex = self.mergeLexicographical(nums1_lex, nums2_lex)

            if merged_lex > res:
                res = merged_lex

        return res

    '''
    Time: O(n)
    Space: O(n)
    '''

    def maxLexicographical(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and num > stack[-1] and k - len(stack) <= N - i - 1:
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack

    '''
    Time: O(n + m) where n is the len of nums1 and m is the len of nums2
    Space: O(n + m)
    '''

    def mergeLexicographical(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mergedArr = []
        ind1, ind2 = 0, 0
        while ind1 < len(nums1) and ind2 < len(nums2):
            if self.greaterLexicographicalList(nums1, nums2, ind1, ind2):
                mergedArr.append(nums1[ind1])
                ind1 += 1
            else:
                mergedArr.append(nums2[ind2])
                ind2 += 1

        if ind1 < len(nums1):
            mergedArr += nums1[ind1:]
        elif ind2 < len(nums2):
            mergedArr += nums2[ind2:]

        return mergedArr

    '''
    returns True if nums1 is  lexicographically bigger than nums2, false if vice versa
    ind1 ; starting index of nums1 subarray
    ind2 ; starting index of nums2 subarray
    '''

    def greaterLexicographicalList(self, nums1: List[int], nums2: List[int], ind1: int, ind2: int) -> bool:
        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] < nums2[ind2]:
                return False
            elif nums1[ind1] > nums2[ind2]:
                return True
            else:
                ind1 += 1
                ind2 += 1

        # nums2 is the longer arr
        if ind1 >= len(nums1):
            return False
        # nums1 is the longer arr
        elif ind2 >= len(nums2):
            return True
        # both are the same length and have the same elements, it doesn't matter what you choose as the biggest
        return True
