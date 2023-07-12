"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str

        1,2,N,3,6,N,7,11,14,N,N,N,N,4,8,12,N,N,N,5,9,13,N,N,10,N,N,N

        (Ex: 7,11,14,N,N,N,N
            order in tree is 3->7->11->14
            - at the end:
            - 14 has no more children, N ; recurse up
            - 11 has no more children, N ; recurse up
            - 7 has no more children, N ; recurse up
            - 3 has no more children, N ; recurse up
            - visit rest of 1 children; new node is 4
        )

        Time: O(n) ; visit every node
        Space: O(1) ; string
        """
        def dfs(node):
            if not node:
                return ",N"

            serialized = "," + str(node.val)
            for child in node.children:
                serialized += dfs(child)
            serialized += ",N"

            return serialized

        serialized_root = dfs(root)
        return serialized_root

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node

        Time: O(n)
        Space: O(n)
        """
        # get rid of first comma
        data = data.split(',')[1:]
        self.i = 0

        def dfs():
            if data[self.i] == 'N' or self.i >= len(data):
                self.i += 1
                return None

            node = Node(data[self.i])
            self.i += 1
            while self.i < len(data) and data[self.i] != 'N':
                child = dfs()
                node.children.append(child)
                self.i += 1

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
