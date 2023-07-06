class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Two Pointers:
        - same as the dynamic approach but using two pointers
        - pointer on left (0) and pointer on right (len(height)-1)
        - while left < right
        - if left height < right:
            if current height >= max left height
                upddate the max left height
            else max left height - current height
            update left+1
        - else
            if current height >=max Right heihgt
                update max right heihgt
            else max right height - current height
            update right+1

        - this solution makes sure that both pointers are aiming for the highest position on the graph
        - if a side is lower than the highest position, then it will be able to find solutions before that highest position
        - this works because it assumes that there will be walls on both ends that stop the water from overflowing but starts 
        without that water from staying

        Contraints:
        - there is atleast 1 height in height list
        - value in height is 0 and positive

        Time: O(n)
        Space: O(1)
        '''

        if not height: return 0

        res = 0
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                res += (maxLeft - height[l])
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                res += (maxRight - height[r])
                r -= 1
        return res


        


