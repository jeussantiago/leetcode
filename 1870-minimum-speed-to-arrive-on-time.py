class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        '''
        - impossible if (len(dist) - 1 > hour)

        - binary search to decide on a speed
        - greedy to figure out if the speed works in the allotted time

        dist = [1,3,2], hour = 2.7

        min=0 ; max=3
        mid=1

        Greedy => 1/1 + 3/1 + 2/1 = 1 + 3 + 2 = 6
        6 > 2.7
            - move min pointer to mid + 1

        min=2 ; max=3
        mid=2
        Greedy => 1/2 + 3/2 + 2/2 = 0.5 + 1.5 + 1 = (round up) = 1 + 2 + 1 = 4
        4 > 2.7
            - move min pointer over

        min=3 ; max=3
        mid=3
        Greedy => 1/3 + 3/3 + 2/3 = 0.33 + 1 + 0.66 = (round up) = 1 + 1 + .66 = 2.66
        2.66 < 2.7
        -------

        dist = [5,10,8], hour = 20
        min=0 ; max=10
        mid=5
        Greedy => 5/5 + 10/5 + 8/5 = 1 + 2 + 1.6 = 1 + 2 + 1.6 = 4.6
        4.6 < (20 + 1)
            - move max speed pointer
            - max = mid
            - keep it part of the solution set

        min=0 ; max=5
        mid=2
        Greedy => 5/2 + 10/2 + 8/2 = 2.5 + 5 + 5 = 3 + 5 + 5 = 13
        13 < (20 + 1)
            - move max pointer

        min=0 ; max=2
        mid=1
        Greedy => 5/1 + 10/1 + 8/1 = 5 + 10 + 8 = 23
        23 > (20 + 1)
            - move left pointer 

        min=2 ; max=2

        - get out of loop b/c l !< r

        1/10000 + 1/10000 + 100000/100000 = 0.1 + 0.1 + 1 = 1 + 1 + 1 = 3 < 3.01

        -----

        - don't round up the last train since we are not waiting for the next train
            - we just have to make it into the office

        n is the length of dist array
        m is the max value is dist array
        Time: O(n logm)
            ; (n) finding max value in dist array
            ; (logm) binaray search starting for max m
            ; (n) greedy calculation
        Space: O(1)
        '''

        if (len(dist) - 1 >= hour):
            return -1

        l, r = 0, 10**7
        res = -1
        while l < r:
            mid = (l + r) // 2

            total_time = self.timeTaken(mid, dist)

            if total_time <= hour:
                r = mid
            else:
                l = mid + 1

        return r

    def timeTaken(self, speed, dist):
        if speed == 0:
            return float('inf')
        total_time = 0
        for i, num in enumerate(dist):
            time_taken = num/speed
            # round every train up except for the last train
            if i < (len(dist) - 1):
                time_taken = math.ceil(time_taken)

            total_time += time_taken

        return total_time

        return 9
