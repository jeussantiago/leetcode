class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''
        Greedy

        Time: O(n)
        Space: O(1)
        '''
        res = 0
        leftBound = minPos = maxPos = -1
        for i, num in enumerate(nums):
            # if num is out of bounds of min and max, start a new subarray
            if num < minK or num > maxK:
                leftBound = i
            # record where the min and max positions are
            if num == minK:
                minPos = i
            if num == maxK:
                maxPos = i
            # check if both min and max positions are part of the new subarray
            if min(minPos, maxPos) > leftBound:
                # the subarray count only starts at the last position of the min and max
                # Ex: nums = [1,1,1,5], minK = 1, maxK = 5
                # would only count if include the 5 but the last 1 is what is important
                # since that can be part of the other 1s but those others 1s cant always be
                # part of the subarray that the last 1 is part of
                res += (min(minPos, maxPos) - leftBound)

        return res


'''
Longer Explanation:

[1,3,2,7,5,0,1,5,0,7]

sliding window:

- check the max
- check the min

if you (start the loop) or the (minVal > than maxK) or (minVal < minK)
    - move the sliding window over by starting the left pointer to after the position
    - left to next index
    (left = i)
    - reset the max
    - reset the min
    (maxVal = float('-inf')
    minVal = float('int'))

- keep the maxVal and minVal positions remembered
- if num == minK
    minPos = i
- same for max

-----------------------------------

Adding to result:
[5,4,3,6,7,8,5,4] ; minK = 4 ; maxK = 8
        |     |   |

- 3 subarrarys
(
    [6,7,8,5,4]
        [7,8,5,4]
        [8,5,4]
)

[5,4,3,6,7,8,5,4,5]
        |     |   |
- you would have the same amount of subarrays as above, but then you would now need to account
for the new subarrays with 5 in it
- 3 subarrarys
(
    [6,7,8,5,4,5]
        [7,8,5,4,5]
        [8,5,4,5]
)
- 6 in total

- after constantly update the min and max positions at each point,
if the minval == min and maxVal is == max
and min(minPos, maxPos) > left
    - res += min(minPos, maxPos) - left

------------------------------------------------

[1,1,1,1] ; mink = 1 ; maxk = 1
[1,1,1,1]
    |
left = -1 ; minPos = -1 ; maxPos = -1 ; res = 0
- update min and max
left = -1 ; minPos = 0 ; maxPos = 0 ; res = 0
- minPos > left => add to res
    - minPos - left = 0 - (-1) = 1
left = -1 ; minPos = 0 ; maxPos = 0 ; res = 1
[1,1,1,1]
    |
- update min and maxPos
left = -1 ; minPos = 1 ; maxPos = 1 ; res = 1
- minPos > left => add to res
    - minPos - left = 1 - (-1) = 2
    - res += 2
left = -1 ; minPos = 1 ; maxPos = 1 ; res = 3
[1,1,1,1]
        |
- update min and maxPos
left = -1 ; minPos = 2 ; maxPos = 2 ; res = 3
- minPos > left => add to res
    - minPos - left = 2 - (-1) = 3
    - res += 3
left = -1 ; minPos = 2 ; maxPos = 2 ; res = 6

[1,1,1,1]
        |
- update min and maxPos
left = -1 ; minPos = 3 ; maxPos = 3 ; res = 6
- minPos > left => add to res
    - minPos - left = 3 - (-1) = 4
    - res += 4
left = -1 ; minPos = 3 ; maxPos = 3 ; res = 10
'''
