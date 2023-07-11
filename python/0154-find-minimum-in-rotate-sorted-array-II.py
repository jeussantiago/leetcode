class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [2,2,2,2,0,1,2]
               |
          [2,2,2,0,1,2]
            [2,2,0,1,2]
              [2,0,1,2]
                [0,1,2]
                   |

        [4,0,1,2,3,4,4,4,4]
          [0,1,2,3,4,4,4,4]
                 |
          [0,1,2]
             |
          [0]



        - if left == right
            - move left an index over
        otherwise, they don't equal each other so we can just act normal

        if mid < right
            right = mid-1
        else
            left = mid+1

        Time: O(logn)
        Space: O(1)
        '''

        minNum = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            minNum = min(minNum, nums[mid])

            if nums[l] == nums[r]:
                # duplicates
                l += 1
            elif nums[l] < nums[r]:
                # array is now sorted in ascending order
                minNum = min(minNum, nums[l])
                break
            else:
                # rotated array
                if nums[mid] <= nums[r]:
                    r = mid-1
                else:
                    l = mid+1

        return min(minNum, nums[r])
