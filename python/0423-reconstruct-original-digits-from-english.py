class Solution:
    def originalDigits(self, s: str) -> str:
        nums = [0 for x in range(10)]
        nums[0] = s.count('z')
        nums[2] = s.count('w')
        nums[4] = s.count('u')
        nums[6] = s.count('x')
        nums[8] = s.count('g')
        nums[3] = s.count('h') - nums[8]
        nums[7] = s.count('s') - nums[6]
        nums[5] = s.count('v') - nums[7]
        nums[1] = s.count('o') - nums[0] - nums[2] - nums[4]
        nums[9] = (s.count('n') - nums[1] - nums[7]) // 2

        res = ""
        for i in range(10):
            res += str(i) * nums[i]
        return res
