class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        DFS w/ caching

        - same concept as below but added caching

        Time: O(n^2)
        Space: (n^2)
            ; (n) recursion stack
            ; (n^2) number of possible values in cache
        '''
        cache = collections.defaultdict(int)

        def dfs(left, right):
            if left == right:
                return nums[left]

            if (left, right) in cache:
                return cache[(left, right)]

            left_simulation_points = nums[left] - dfs(left + 1, right)
            right_simulation_points = nums[right] - dfs(left, right - 1)

            cache[(left, right)] = max(
                left_simulation_points, right_simulation_points)
            return cache[(left, right)]

        return dfs(0, len(nums) - 1) >= 0


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        DFS

        - each player has the option of choosing the left or right end
        - in recursion, keep track of the left and right pointers

        - base case
            - left == right: then doesnt matter which one you return, return nums[left]

        - simulate player choosing left, recurse by moving left pointer over
        - simulate player choosing right, recurs by moving right pointer leftwards

        - we want to keep track of the max amounts of points a player can achieve since
        theyre playing optimally to win

        - return the max of the left side and the right side

        - since theres 2 people, we can offset each others amount of points by subtracting the
        current num choice (left or right) by the max amount of points the other player can receive
        in their turn

        - at the end, if the total is >= 0, it means player 1 won
        - if negative, means player 1 lost

        Time: O(2^n)
            ; (2^n) 2 choices, height of tree is n
        Space: O(n)
            ; (n) recursion stack
        '''

        def dfs(left, right):
            if left == right:
                return nums[left]

            left_simulation_points = nums[left] - dfs(left + 1, right)
            right_simulation_points = nums[right] - dfs(left, right - 1)

            return max(left_simulation_points, right_simulation_points)

        return dfs(0, len(nums) - 1) >= 0
