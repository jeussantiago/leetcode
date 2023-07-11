class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        l, r = 2, num // 2
        while l <= r:
            mid = l + (r - l) // 2
            guess = mid * mid

            if guess == num:
                return True
            elif guess > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
