# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        '''
        address_indx = {
            address: [indx]

            0x7fb: 0
            0x7fb: 2
            0x7fb: 4
            0x7fb: 5

        }

        clone_indx_address = {
            0: root
            2: node(1, left=None, right)
            4: node(empty)
        }

        RECURSION

        - insert the val

        - if left exist:
            if not clone_indx_address[address_indx[curr_node]]
            (node doesn't exist in our tree)
                - create a empty left node
                Node()
                - insert key(index of right) : val(node)
            - point left to that node

        - if right exist:
            if not clone_indx_address[address_indx[curr_node]]
            (node doesn't exist in our tree)
                - create a empty right node
                Node()
                - insert key(index of left) : val(node)
            - point right to that node

        - if random exist
            random_index = address_indx[node.random]
            if not clone_indx_address[random_index]
            (node doesn't exist in our tree)
                - check the index of the random node
                - create the empty random node
                Node()
                - insert key(index of random) : val(node)

            - point random to that node

        - recurse through left nodes
        - recurse through right nodes

        Time: O(n)
        Space: O(n)
        '''
        if not root:
            return root

        cloned_addresses = {}

        def cloneNode(node):
            if not node:
                return None
            if node not in cloned_addresses:
                cloned_addresses[node] = NodeCopy(val=node.val)
            return cloned_addresses[node]

        def cloneTree(node, clone):
            if not node:
                return
            # make copies of children
            clone.left = cloneNode(node.left)
            clone.right = cloneNode(node.right)
            clone.random = cloneNode(node.random)

            # recurse through tree
            cloneTree(node.left, clone.left)
            cloneTree(node.right, clone.right)

        clone = NodeCopy(val=root.val)
        cloned_addresses[root] = clone
        cloneTree(root, clone)
        return clone
