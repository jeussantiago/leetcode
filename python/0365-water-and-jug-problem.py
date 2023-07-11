class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        '''
        3, 5 = 2
        2, 3 = 1
        1, 2 = 1
        1, 1 = 0
        0, 1
        return 1

        2, 6 = 4
        4, 1 = 0
        0, 4
        return 4


        '''
        def gcd(n1, n2):
            if n1 == 0:
                return n2
            return gcd(n2 % n1, n1)

        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        common = gcd(jug1Capacity, jug2Capacity)
        return targetCapacity % common == 0
