# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        '''
        Logical Deduction:
        - we can assume at the beginning the person 0 is the celebrity
        - if person 0(assumed celebrity), knows someone, then person 0 is not the celebrity
        - this means that the person that person 0 knows, is possibly the celebrity
        - so we can assume this person as the celebrity and proceed to check every other guest

        assumed_celebrity = 0
        - go through every guest except self
            - if knows(assumed_celebrity, person_i)
            (assumed_celebrity knows person_i -> assumed_celebrity is not celebrity, but person_i might be)
                assumed_celebrity = person_i

        - but we still don't know for certain if this person is a celebrity
            - everyone needs to know this person
            - and the celebrity doesn't need to know anyone
            - do the brute force method

        Time: O(n + n) narrowing down the celbrity candidate + making sure the person is acutally a celbrity
            : O(n)
        Space: O(1)
        '''
        # narrow down the celbrity candidate
        assumed_celebrity = 0
        for person in range(1, n):
            if knows(assumed_celebrity, person):
                assumed_celebrity = person

        # make sure assumed_celebrity is actually a celbrity
        for person in range(n):
            if person == assumed_celebrity:
                continue
            if knows(assumed_celebrity, person) or not knows(person, assumed_celebrity):
                return -1

        return assumed_celebrity


class Solution:
    def findCelebrity(self, n: int) -> int:
        '''
        Brute Force:
        - ask everyone if they know someone
        - since the celebrity doesn't know anyone, if the API returns true, then 
        this person cannot be the celebrity
        T: O(n^2)
        S: O(1)
        '''

        def helper(people, person):
            for i in range(people):
                if i == person:
                    continue
                # person knows someone - the celebrity wouldn't know anyone
                # the someone doesn't know the celebrity - everyone knows the celebrity
                if knows(person, i) or not knows(i, person):
                    return False

            # person knows no one - must be the celebrity
            return True

        for i in range(n):
            if helper(n, i):
                return i
        return -1
