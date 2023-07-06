class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        n is the size of nums1
        m is the size of nums2
        Time: O(log(min(n, m)))
        space: O(1)
    
        '''
        #binary search to find point where x1 <= y2 and y1 <= x2
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        #assume B is always bigger than A
        if len(A) > len(B):
            A, B = B, A

        #run binary serach on smaller Array (A in this case) - get pointers
        l, r = 0, len(A) - 1

        while True:
            #get middle value for A
            i = (l + r) // 2
            #get middle value for B (-2 b/c len of both arrays together)
            j = half - i - 2

            #set partitions
            #any of these indices could be out of bounds (i < 0 or >+ len(array))
            Aleft = A[i] if i>= 0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j>= 0 else float("-infinity")
            Bright = B[j+1] if (j + 1) < len(B) else float("infinity")

            #check if the partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                #even - want decimal so do normal diivsion
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            #didnt find median, partiion is incorrect - Aleft is too big (too many elements)
            elif Aleft > Bright:
                #reduce size of left partiion
                r = i - 1
            #Aleft is too small
            else:
                #increase size of right partiion
                l = i + 1

            # A = [1, 2, 3(left), 4(right), 5, 6] and B = [1, 2(left), 3(right), 4, 5]
            # r = 3 - 1 = 2(i.e. index 0,1,2) --> A = [1, 2(L), 3(R), 4, 5, 6] and B = [1, 2, 3(L), 4(R), 5, 6]
                

