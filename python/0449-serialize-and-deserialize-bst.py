# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        Time: O(n)
        Space: O(n)
        """
        encoded = []

        def dfs(node):
            if not node:
                encoded.append("N")
                return

            encoded.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(encoded)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        Time: O(n)
        Space: O(n)
        """
        data = data.split(',')
        self.i = 0

        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return

            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
