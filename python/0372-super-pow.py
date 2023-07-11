class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        expo = 0
        for num in b:
            expo = (expo * 10) + num

        return pow(a, expo, 1337)
