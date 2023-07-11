# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    - build a tree from preorder
    - there was a problem where you can build a tree from an inorder and preorder list. However, you needed those two
    to create a tree b/c you didn't know where the Null values were
    - we can create a tree from preorder traversal list if the null values are include
        - traverse left and keep adding the nodes, when you hit a null, go to the right nodes

    N => Null node
    Example 1:
    serialize:
    =>  "1,2,N,N,3,4,N,N,5,N,N"

    deserialize:
    =>  - keep adding the nodes to the left side of the tree until you hit a null
        - when you hit a null, go back up the tree to it's parent and go to the right side of the tree
        - repeat this process

                    1
            2                   3
        N       N           4
                        N       N 

    '''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        T: O(n) where n is the number of nodes in the tree
        S: O(1)
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(",".join(res))
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        T: O(n)
        S: O(n) creating the tree
        """
        data = data.split(",")
        self.ind = 0

        def dfs():
            if data[self.ind] == "N":
                self.ind += 1
                return None

            node = TreeNode(int(data[self.ind]))
            self.ind += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
