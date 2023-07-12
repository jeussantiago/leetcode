class UnionFind:
    def __init__(self, n):
        self.group = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
        self.num_non_connected_nodes = n - 1

    def find(self, node):
        # if parent != child
        if self.group[node] != node:
            # set parent of child to be the grandparent
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            # repeat edge
            return 0

        if self.rank[parent1] < self.rank[parent2]:
            self.group[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        else:
            self.group[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]

        # new edge connnection
        self.num_non_connected_nodes -= 1
        return 1

    def visited_all_nodes(self):
        return self.num_non_connected_nodes == 0


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        Union Find

        -  if edge1 parent == edge2 parent
            - this edge is not required
        - if edge1 parent != edge2 parent
            - this edge is required
            - add to the number of connected nodes


        k is the length of edges list
        Time: O(n + k)
                ; (n) to create the group and rank list for both alice and bob
                ; (k) go through all elements in edges_list - join operations are O(1)
                ; (1) check if all the nodes have been visited
        Space: O(n) ; (2n) rank and group list each for alice and bob
        '''
        alice, bob = UnionFind(n), UnionFind(n)
        edges_required = 0
        # we have 2 loops because the edges that can be traversed by both bob and alice are much more important that the single traverse edges
        # they take priority so we would want to count these rather than count the other single edges that do the same thing
        # those single would be useless Ex: [1,1,2] and [3,1,2] => [1,1,2] is a useless edge, but it can appear in the list much earlier than
        # the double traversed edge so doing this to take priority
        for typ, node1, node2 in edges:
            if typ == 3:
                # both can traverse - "|" rather than "or" allows both of the joins to process
                edges_required += (alice.join(node1, node2)
                                   | bob.join(node1, node2))

        for typ, node1, node2 in edges:
            if typ == 2:
                # Bob can only traverse
                edges_required += bob.join(node1, node2)
            else:
                # Alice can traverse
                edges_required += alice.join(node1, node2)

        # check if all the nodes have been visited
        if alice.visited_all_nodes() and bob.visited_all_nodes():
            return len(edges) - edges_required

        return -1
