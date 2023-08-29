class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''
        binary search

        - sort heaters
        - for each house, use binary search to find the closest heater to itself
        - once found, calculate distance
        - keep track of max distance
        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) for each house
            ;   (logn) binary search
        Space: O(1)
        '''
        heaters.sort()
        res = 0
        for house in houses:
            l, r = 0, len(heaters) - 1
            minRadius = float('inf')
            while l <= r:
                mid = (l + r) // 2
                minRadius = min(minRadius, abs(house - heaters[mid]))
                if heaters[mid] == house:
                    break
                elif heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid - 1

            res = max(res, minRadius)

        return res
