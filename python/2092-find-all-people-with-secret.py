class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        '''
        Union Find

        n is the number of people
        m in the number of meetings
        Time: O(m^2)
            ; (mlogm) sort meetings so that earliest times come first
            ; (m) iterate through meetings
            ; (1) insert person into union find
        Space: O(n)
            (n) array to store if person knows secret
            ; (n) array to store the parent 
        '''
        # early meetings first
        meetings.sort(key=lambda x: x[2])

        # we need to know which meetings all happen at the same time
        # this is so we can check if there is a connection for anyone to person 0
        # who knows the secret
        same_meeting_time = collections.defaultdict(list)
        for person1, person2, meeting_time in meetings:
            same_meeting_time[meeting_time].append((person1, person2))

        uf = UnionFind(n)
        # create a connection with the first person
        uf.union(0, firstPerson)

        for meeting_time, meeting_participants in same_meeting_time.items():
            # create a connection between the people in the meeting
            for person1, person2 in meeting_participants:
                uf.union(person1, person2)

            # check if the, now connected participants, are connected to person 0
            for person1, person2 in meeting_participants:
                # only need to check one person since they're both connected
                if not uf.hasSameParent(0, person1):
                    uf.resetConnection(person1)
                    uf.resetConnection(person2)

        knows_secret = []
        for person in range(n):
            if uf.hasSameParent(0, person):
                knows_secret.append(person)

        return knows_secret


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        # don't need to do anything since both parents point to person 0
        if parent1 == parent2:
            return

        # create a connection
        if self.rank[parent1] >= self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]

    def hasSameParent(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def resetConnection(self, node):
        self.parent[node] = node
        self.rank[node] = 1
