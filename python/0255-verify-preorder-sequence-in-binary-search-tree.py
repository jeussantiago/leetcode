class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        '''
        [44,22,11,66,55,33,77,88]
        Valid BST:
            - every left node should be < than parent
            - every right node should be > than parent

        - if the current node is < than previous
            - add to stack
        - if the current node is > than previous
            - remove all the items from the stack until we find the current node's parent

            - if the current node  <  the parent
                - nonValid Tree
                - return False

        - keep track of the previous parent

        [50,75,72,70,89,71]
        50
            75
          72     89
        70      71

        - although 71 is < 89, which is fine
        - 71 is not > 75, which was the previous parent which is an issue and makes it a none valid tree

        - if the current node is > than the previous node(in the stack)
            - find the new parent to compare every afterwards

        - if the current node < than the parent
        (although at the current iteration, it won't be true, we are using this to compare future numbers
        in the case above, we compared 71 to 75 and not it's parent)
            - return False
            (non Valid tree)

        Time: O(n)
        Space: O(n)
        '''

        parent = None
        stack = []
        for node in preorder:
            while stack and node > stack[-1]:
                parent = stack.pop()

            if parent and node < parent:
                return False

            stack.append(node)
        return True
