class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        '''
        Topological Sort:

        - Items that don’t belong to a technically still belong to a group. They just have their own group. But we can’t have them all stay on group -1 otherwise it looks like they belong to the same group 
        -         Replace the -1 with a group id that is not being used. Can start group_id at m value since that tells us how many actual groups there are

        group = [-1,-1,1,0,0,1,0,-1]
        group = [2, 3, 1, 0, 0, 1, 0, 4]

        We need to Topologically sort the nodes themselves but there’s also the constraint that nodes that are part of the same group need to be next to each other. So we can topologically sort the groups too. 

        Topological sort uses indegrees(BFS) to figure out which nodes are last. We can create a list for the indegrees of a node. And another list to contain that nodes that come before the current node. We do this for both nodes and groups

        Nodes_graph: add current node  to key=prev_node in beforeItems(current_node) 
        Node_indegree: increase count for current node

        If the group of current_node != prev_node:
        Group_graph: add groups[curr_node] to key=groups[prev_node] 
        Group_indegree: increase count for current group

        beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

        Item_graph = [[], [], [], [4], [], [2], [1, 3, 4], []]
        Item_indegree  = [0, 1, 1, 1, 2, 0, 0, 0]

        Group_graph = [[3], [], [], [], [], [], [], []]
        Group_indegree = [0, 0, 0, 1, 0, 0, 0, 0]

        Sort the Items and Groups based on the graphs and indegree

        Topological sort:
        Queue node with indegree of 0. That will be our first. Add the neighbors to the queue if not visited and keep decreasing the indegree count. Repeat

        If the length of visited != length of graph
        - impossible so return []
        - Otherwise return the visited

        item_order = [7, 6, 5, 0, 1, 3, 2, 4]
        group_order = [7, 6, 5, 4, 2, 1, 0, 3]

        Ordered_groups to sort based on the groups and items from topological sort.
        - now the numbers in each group is sorted
        {4: [7], 
        0: [6, 3, 4], 
        1: [5, 2], 
        2: [0], 
        3: [1]} 

        based on the ordering in group_order, get the corresponding data from ordered_groups using key=group_order i
        [7, 6, 5, 4, 2, 1, 0, 3]
        [[], [], [], [7], [0], [5, 2], [6, 3, 4], [1]]
        [7, 0, 5, 2, 6, 3, 4, 1]

        n is the number of groups
        Time: O(n^2)
            ; (n^2) build adj list for corresponding node and prev_connecting_node
            ; (n^2) topological sort - worst case could have every node be a prev node of the curr node 
        Space: (n)
            ; (n^2) worst case the adj list can contain each node and a list of every other node
            ; (n) storing in degree
            ; (n) queue

        '''

        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                # (prev -> curr) represents an edge in the item graph
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # If they belong to different groups, add an edge in the group graph.
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topologicalSort(graph, indegree):
            visited = []
            queue = collections.deque(
                [node for node in range(len(graph)) if indegree[node] == 0])
            while queue:
                curr_node = queue.pop()
                visited.append(curr_node)
                for next_node in graph[curr_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.appendleft(next_node)

            if len(visited) == len(graph):
                return visited
            return []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        res = []
        for group_index in group_order:
            res += ordered_groups[group_index]

        return res
