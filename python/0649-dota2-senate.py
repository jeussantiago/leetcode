class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        2 Queue
        Time: O(n)
        Space: O(n)
        '''
        # senate = "RDRD"
        N = len(senate)
        radiant = collections.deque([])
        dire = collections.deque([])
        for i, team in enumerate(senate):
            if team == "R":
                radiant.appendleft(i)
            else:
                dire.appendleft(i)

        while radiant and dire:
            radiant_senate, dire_senate = radiant.pop(), dire.pop()
            if radiant_senate < dire_senate:
                # place the radiant senate back into the queue keeping the relative order the same, thats why we increase ind value with N
                radiant.appendleft(radiant_senate + N)
            else:
                dire.appendleft(dire_senate + N)

        if radiant:
            return "Radiant"
        return "Dire"
