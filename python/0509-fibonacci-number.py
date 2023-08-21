class Solution:
    def fib(self, n: int) -> int:

        self.cache = {
            0: 0,
            1: 1
        }

        def helper(N):
            if n in self.cache:
                return self.cache[N]

            self.cache[N] = self.fib(N-1) + self.fib(N-2)
            return self.cache[N]

        return helper(n)
