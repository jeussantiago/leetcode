class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        - sort by descending height and increasing k
        - insert person at the index of k

        [[5,0],[4,4],[7,1],[7,0],[6,1],[5,2]]
        [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

        [[7,0],[7,1]]
        [[7,0],[6,1],[7,1]]
        [[5,0],[7,0],[6,1],[7,1]]
        [[5,0],[7,0],[5,2],[6,1],[7,1]]
        [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

        Time: O(n^2)
            ; (nlogn) python sorting 
            ; (n^2) queue construction - insert takes (n) time
        Space: O(n)
            ; (n) python sorting
            ; (n) queue construction
        '''

        people = sorted(people, key=lambda x: (-x[0], x[1]))

        res = []
        for person in people:
            res.insert(person[1], person)

        return res
