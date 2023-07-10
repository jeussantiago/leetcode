class Solution:
    def numTrees(self, n: int) -> int:
        '''
        - diagram is created because at each root, the next number is bigger or less than the node

        n  |  # trees
        -------------
        1       1
        2       2
        3       5

        1 2 3 4 5
        - every node will be the root at some point
        if root == 2
        - 1 would go in its left subtree
        - 3, 4, 5 would go in its right subtree
        - number of unique trees created if root==2 would be
        numTrees(1) * numTrees([3,4,5])
        (we know at n==1, # trees would be 1)
        (we know at n==3, # trees would be 5)
        1 * 5 = 5
        - if root==2, there would be 5 unique subtrees
        - now apply that logic to every possible noode



        Time: O(n^2)
        Space: O(n)

        numTrees[4] = numTrees[0] * numTrees[3] +
                      numTrees[1] * numTrees[2] +
                      numTrees[2] * numTrees[1] +
                      numTrees[3] * numTrees[0] 

        [1,1,1]
        tree = [1,2]
        when n == 2:
        (0 elements is 1 unique tree)
        if root == 1: left subtree has 0 elements * right subtree at 1 element = 1
        if root == 2: left subtree has 1 elements * right subtree at 0 elements = 1
        - save to total
        - at end, save to cache so that you now know the case if n == 2
        - this will help with n==3 and so on

        '''
        # we initialize the values in the dp chache to 1 is because of the base case of if n==1 or 0
        numTree = [1] * (n+1)

        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]
