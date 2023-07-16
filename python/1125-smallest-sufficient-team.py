class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        '''
        DP Bitmask      

        - turn each list of people into a bitmask based on the requirements
        people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

        people = [111000, 110100, 001011, 000110, 010010, 001001]

        - start with req_skills to be just 0
        req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
        req_skills = [0,0,0,0,0,0]

        a b c
        1 1 1

        n = 3 (the number of skills)
        1 << 3 == 8
            - this 8 represents the number of different combinations

        0 0 0
        0 0 1
        0 1 0
        ...
        1 1 1 == 7

        - this is how we get the size of our dp
        - iterate over all combinations whether that person has the skillset or not
            - check if the person's skill are covered by the current team in dp

        '''

        n = len(people)
        m = len(req_skills)
        skill_id = {skill: i for i, skill in enumerate(req_skills)}

        # turn all teams in people array into bits
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        # create a dp of the possible combinations of required skills
        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0

        # iterate over all combinations whether that person has the skillset or not
        for skills_mask in range(1, 1 << m):
            # check if the person's skill are covered by the current team in dp
            for i in range(n):
                # remaining skills required after considering the person
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                # the person's skill are not fully covered by the team, so you can add this person to the team
                if smaller_skills_mask != skills_mask:
                    # add the person to the team (1 << i) representing the person's index position in people array
                    # by updating the bitmask position number of the combination of this person being considered
                    people_mask = dp[smaller_skills_mask] | (1 << i)
                    # update the current dp position with the bitmask that has the fewest bit count (# of 1s)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        # get the people who are added to the team
        # each position in the final_team represents the person that was added to the team
        final_team = dp[(1 << m) - 1]
        res = []
        for i in range(n):
            if (final_team >> i) & 1:
                res.append(i)

        return res
