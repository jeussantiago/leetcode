"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        - have a queue to iterate the nodes/neighboring nodes
        - iterate over the nieghbors of the current node
        - if the neighboring nodees don't exist in the hash table, 
            - create a node for them
            - add those nodes to the queue

        - at this point, new nodes have created copies and already seen nodes already have copies
        - for each neighbor, add the hashtable[node.val] to the current node's list

        Time: O(n)
        Space: O(n)
        '''
        if not node:
            return node

        q = collections.deque([node])
        clone = {}
        clone[node.val] = Node(node.val)

        while q:
            curr_node = q.pop()
            for neighboring_nodes in curr_node.neighbors:
                if neighboring_nodes.val not in clone:
                    # create a node for its neighbors
                    clone[neighboring_nodes.val] = Node(neighboring_nodes.val)
                    q.appendleft(neighboring_nodes)
                clone[curr_node.val].neighbors.append(
                    clone[neighboring_nodes.val])

        return clone[node.val]
