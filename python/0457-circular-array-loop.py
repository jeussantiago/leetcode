class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
        slow and fast pointer

        Time: O(n)
            ; every position gets visited once
        Space: O(n)
            ; visited set same size as nums list
            ; cycle dict can be at most the size of n
        '''

        for i, num in enumerate(nums):
            direction = 1 if num > 0 else -1
            slow = fast = i

            while True:
                slow = self.getNextInd(nums, slow, direction)
                fast = self.getNextInd(nums, fast, direction)

                if fast != -1:
                    fast = self.getNextInd(nums, fast, direction)

                # slow and fast are in cycle
                # slow or fast is out of bounds
                if slow == -1 or fast == -1 or slow == fast:
                    break

            # slow and fast pointers are the same and they are not out of bounds
            if slow == fast and slow != -1:
                return True

        return False

    def getNextInd(self, nums, ind, direction):
        N = len(nums)
        next_ind = (ind + nums[ind]) % N
        if next_ind < 0:
            next_ind += N

        # if the prev direction was positive and new direction/value goes in the opposite direction, there is a loop
        # if the direction is same, positive w/ positive and negative w/negative then there can't be a loop
        # loop containing itself (self-loop)
        if (
            (nums[next_ind] * direction) <= 0 or
            next_ind == ind
        ):
            return -1

        return next_ind
