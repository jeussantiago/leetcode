class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        '''
        - might have a case where the further back monsters walk faster than the 
        monsters initially closer to the city
        (this is why you can't solve it straight up greedily)

        dist =  [2,4,6,8,10,12]
        speed = [2,2,2,2,2, 5]
        - you can hit the first 2 monsters
        - then the third monster and the last monster are both going to be 2km away
        from the city -> they move fast enough that in the next minute they will
        both be 0km away from the city
            - so you can only hit one of them then the game ends

        - another case is if they are far enough from the city and move slow enough that you
        can hit the front one and reload before the second one reaches your city even if they
        have the same speed and same distance
        dist =  [10,10,10]
        speed = [ 7, 7, 7]

        Solution:
        - create a new array with how many minutes it takes for a monster to reach a city
        [1,2,3,4,5,3]
        - we can fire a shot at each minute
        (we don't need a new variable, we can just use the range length as the tracker/counter)
        - greedily check if the difference between the current time is atleast 1 min difference 
        from the time the current weapon is able to fire

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) creating time to city array
            ; (n) calculating how many shots to fire
        Space: O(n)
            ; (n) creating time to city array
        '''
        time_to_city = [km / hr for km, hr in zip(dist, speed)]
        time_to_city.sort()

        shots = 0
        for i in range(len(time_to_city)):
            if time_to_city[i] <= i:
                # not enough time to load weapon and fire
                break

            shots += 1

        return shots
