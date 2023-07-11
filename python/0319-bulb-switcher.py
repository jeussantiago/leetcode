class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''
        0,0,0,0,0,0,0,0,0,0,0,0 
        1,1,1,1,1,1,1,1,1,1,1,1 ; n=1
        1,0,1,0,1,0,1,0,1,0,1,0 ; n=2
        1,0,0,0,1,1,1,0,0,0,1,1 ; n=3
        1,0,0,1,1,1,1,1,0,0,1,0 ; n=4
        1,0,0,1,0,1,1,1,0,1,1,0 ; n=5
        1,0,0,1,0,0,1,1,0,1,1,1 ; n=6
        - at the half way point, you just flip everything
        1,0,0,1,0,0,0,1,0,1,1,1 ; n=7
        1,0,0,1,0,0,0,0,0,1,1,1 ; n=8
        1,0,0,1,0,0,0,0,1,1,1,1 ; n=9
        1,0,0,1,0,0,0,0,1,0,1,1 ; n=10
        1,0,0,1,0,0,0,0,1,0,0,1 ; n=11
        1,0,0,1,0,0,0,0,1,0,0,0 ; n=12

        - since the bulbs are initally off, at the end, only the bulbs that are toggled an odd number of times will be on
            - we need to find bulbs which have an odd number of factors (how many times the bulb will be flickered)

        Time: O(1)
        Space: O(1)
        '''
        return int(sqrt(n))
