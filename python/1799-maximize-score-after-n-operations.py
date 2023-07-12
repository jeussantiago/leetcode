class Solution:
    def maxScore(self, nums: List[int]) -> int:
        '''
        can use bitmask idea to cahce 

        [1,2,3,4,5,6]

        - in one path we can first take 1,3. then we take 2,4 in the second round
        - in another path we can first take 1,2. then take 3,4 in the second round
        - in both rounds, 5,6 are left so that would make it repeated work
        - need some method to remember this repeated work => bitmask
            - we can turn each position in the array to 0=not_used and 1=used  as the key for the cache
            [1,2,3,4,5,6]
            [1,1,1,1,0,0]

        - there is an idea to store the current operation step with the key
            - however, that is not needed since to get to a specific bitmask, it takes the same exact number of operations to get 
            to the same bitmask (similar to above)
            - so storing the current opearation woudl be redundant info

        00000 &
          100  
        => 0 => Non used number

        00100 &
          100  
        => 1 => Used number

        n is the length of nums array
        Time: O(n^2 * 2^n) 
                ; (2^n) the number of possible values in the bitmask, can for each number, can decide to include or not include
                ; (n^2) at each step, we have to pair up 2 numbers, 
                        so go through arr to choose 1 num then go through again to choose second number
                ; (log(max(x,y))) GCD-> greatest common divisor

        Space: O(2^n)
                ; bitmask possibilities
        '''
        N = len(nums)
        cache = collections.defaultdict(int)

        def dfs(bitmask, op):
            if bitmask in cache:
                return cache[bitmask]

            for i in range(N):
                for j in range(i + 1, N):
                    # check if numbers have been used before
                    if (1 << i) & bitmask or (1 << j) & bitmask:
                        continue

                    # numbers have not been used before
                    # calculate the score
                    score = op * math.gcd(nums[i], nums[j])
                    # new bitmask with the numbers turned to 1 to show that they're used
                    new_bitmask = bitmask | (1 << i) | (1 << j)
                    # go to next set of numbers to get their score
                    cache[bitmask] = max(
                        cache[bitmask],
                        score + dfs(new_bitmask, op + 1)
                    )

            return cache[bitmask]

        return dfs(0, 1)
