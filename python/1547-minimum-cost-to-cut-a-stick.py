class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        Top Down memoization

        Time: O(m^3)
            ; (m^2) try all possible values for the cahce, (left, right)
            ; (m) for each position, we need to go through the rest of the cuts between inndex left and index right
        Space: O(m^2)
            ; all possible (left, right) solutions in cache
        '''
        cuts = [0] + sorted(cuts) + [n]
        cache = {}

        def get_cuts(left, right):
            if (left, right) in cache:
                return cache[(left, right)]

            # if theres only 1 item in the subarray then we can't cut anymore
            if right - left == 1:
                return 0

            # we don't want to include the left and right indexes since they could possibly contian 0, n, and the mid which is where the precious cut is located
            # (which we don't want to factor in anymore)
            min_cost = float('inf')
            for mid in range(left + 1, right):
                cost = (
                    (cuts[right] - cuts[left]) +
                    get_cuts(left, mid) +
                    get_cuts(mid, right)
                )
                min_cost = min(min_cost, cost)

            cache[(left, right)] = min_cost
            return min_cost

        return get_cuts(0, len(cuts) - 1)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        [5,6,1,4,2]
        [1,2,4,5,6] ; n=9 ; +9
        [1,2] l=0 h=4 ; +4           [5,6] l=4 h=9 ; +5
        [1] l=0 h=2 ; +2                [5] l=4 h=6 ; +2
        []                              []

        - sort cuts array

        Keep track of:
            - low and high number values
            - subset of the array

        recursion:
            - stop the recursion when the subarray is empty
            (gone through all of the cuts)
                - return 0

            - don't need a cahce

            - get the mid value from the low and high values
            - see where the mid value fits into the current subarray
                - bisect_left

            - call new recursion with left side of mid point/bisect 
                low=same ; high= value at mid index ; new_subarray= sub[:mid_ind]
            - and right side of mid point/bisect
                low=value at mid index ; high=same ; new_sub = sub(mid_ind + 1:)

            - return the length of the stick when made these cuts
            return high - low

        n is the max number of cuts in the cuts array
        Time: O(nlogn)
            ; (nlogn) sorting
            ; (nlogn) recurison is done (n) number of times since we don't do a re-cut at a position that has already been used
                ; (logn) binary search to find the mid index
        Space: O(n)
            ; (n) python sorting
            ; (logn) recursion
        '''
        def cut_sticks(low, high, sub):
            print(low, high, sub)
            if not sub:
                return 0

            mid = (low + high) // 2
            mid_ins = min(bisect_left(sub, mid), len(sub) - 1)
            # stick lenght/cost of cut + left cost after cut + right cost after cut
            return (
                (high - low) +
                cut_sticks(low, sub[mid_ins], sub[:mid_ins]) +
                cut_sticks(sub[mid_ins], high, sub[mid_ins + 1:])
            )

        cuts.sort()
        print(n, cuts)

        return cut_sticks(0, n, cuts)
