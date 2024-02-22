class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        t is the length of trust
        Time: O(t + n)
        Space: O(1)
            ; hashmaps are going to contain the number of people, which is max 1000
        '''
        if len(trust) == 0 and n == 1:
            return n

        T = len(trust)
        possible_judge = collections.defaultdict(int)
        definitely_not_judge = set()
        for person_a, person_b in trust:
            # since person_a trust person_b, person_a can't be the judge
            definitely_not_judge.add(person_a)
            # since the trust is unique, we don't need to keep track of the
            # specific people who trust person_b, just the count is fine
            possible_judge[person_b] += 1

        # go through the possible judge to find the judge
        judge = -1
        for person, trust_cnt in possible_judge.items():
            # everyone trust this person except the judge
            if person not in definitely_not_judge and trust_cnt == n - 1:
                if judge != -1:
                    # another person who fit the judge position
                    # there can only be one
                    return -1

                judge = person

        return judge
