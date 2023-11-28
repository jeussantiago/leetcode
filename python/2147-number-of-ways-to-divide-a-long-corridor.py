class Solution:
    def numberOfWays(self, corridor: str) -> int:
        '''
        DFS

        Time: O(n)
            ; (2n) number of seats from 1-2
        Space: O(n)
            ; recursion stack
            ; cache
        '''
        MOD = 10 ** 9 + 7
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def dfs(i, seats):
            if i == len(corridor):
                # if seats == 2, return 1, otherwise number of seats is odd
                return 1 if seats == 2 else 0

            if cache[i][seats] != -1:
                return cache[i][seats]

            res = 0
            if seats == 2:
                if corridor[i] == "S":
                    res = dfs(i + 1, 1)
                else:
                    # plant, can either add a divider or move on
                    res = (dfs(i + 1, 0) + dfs(i + 1, seats)) % MOD
            else:
                # not enough seats to add a corridor
                if corridor[i] == "S":
                    res = dfs(i + 1, seats + 1)
                else:
                    res = dfs(i + 1, seats)

            cache[i][seats] = res
            return res

        return dfs(0, 0)


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        '''
        Greedy:

        - count how many seats there are
            - if odd: can have exactly 2 seats => return 0
            - if seats <= 1: return 0
            - if seats == 2: return 1

        - now we can gurantee that we can put up a divider
        - for each set of 2 seats, you need to find the number
        of plants between the closest seats
            - In example 1, theres 2 plants in between
            - Lets say that the input is changed: 
            corridor = "SSPPSPSPPPSS"
            - this means that the number of plnts between the second set of 
            seats and the third set of seats is 3 plants which is 4 corridors

            - we can just multiply the possible combinations to find
            the number of ways to divide a corridor
            (example solution is 12)

        Time: O(n)
        Space: O(1)
        '''
        MOD = 10 ** 9 + 7

        seat_count = corridor.count("S")
        if seat_count % 2 or seat_count <= 1:
            return 0

        res = 1
        last_seat_ind = -1
        seat_count = 0
        for i, item in enumerate(corridor):
            if seat_count == 2:
                if item == "S":
                    plant_count = i - last_seat_ind
                    res = (res * plant_count) % MOD
                    seat_count = 1
                    last_seat_ind = i

            else:
                if item == "S":
                    seat_count += 1
                    last_seat_ind = i

        return res
