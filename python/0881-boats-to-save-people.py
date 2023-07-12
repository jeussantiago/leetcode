class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        - keep adding the heaviest people
        - onlly addd the lightest people when you can't add any more heavy people
        - each boat carries 2 people max

        Time: O(nlogn) ssorting is nlogn, the algorithm afterwards is O(n)
        Space: O(n) sorting takes logn of extra space, (I think in other languages) - python sorting takes O(n) space since it uses Timsort Algorithm
        '''

        people.sort()

        l, r = 0, len(people)-1
        boats = 1
        total_weight = 0
        num_people_on_boat = 0
        while l <= r:
            if total_weight + people[r] <= limit and num_people_on_boat < 2:
                total_weight += people[r]
                num_people_on_boat += 1
                r -= 1
            elif total_weight + people[l] <= limit and num_people_on_boat < 2:
                total_weight += people[l]
                num_people_on_boat += 1
                l += 1
            else:
                boats += 1
                total_weight = 0
                num_people_on_boat = 0

        return boats
