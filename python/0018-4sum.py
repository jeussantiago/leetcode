class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        1) atleast 1 number in nums
        2) num in nums in range of -10^9 - 10^9
        3) similar conditions for target
        4) a,b,c,d are different indexes

        two approches:
        1) recursion
        2) 2 for loops and a while loop with ponters
        both have Time: O(n^3)
        '''

        nums.sort()
        res, quad = [], []
        #target as a parameter because target will be changing depending on the values we need
        def kSum(k, start, target):
            #(non base case)
            if k != 2:
                #nums - k, because we want to leave enough space for the other values i.e. 4, leave space for the other 3 characters
                for i in range(start, len(nums) - k + 1):
                    #skip repeating characters, make sure not to go out of bounds by being at the start - skip iteration of loop
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    #add number to current array
                    quad.append(nums[i])
                    #look for less numbers(we found one value), go to next index in array to look for next number, look for new target
                    kSum(k-1, i+1, target-nums[i])
                    #clean up array created
                    quad.pop()
                return
            #base case - Two Sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    #combine 2 list and add to the results
                    res.append(quad + [nums[l], nums[r]])
                    #doesnt matter which pointer we move
                    l += 1
                    #keep incrementing pointer until number is not the same anymore
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4, 0, target)
        return res

            