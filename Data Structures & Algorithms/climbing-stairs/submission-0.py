class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        first = self.climbStairs(n-1)
        second = self.climbStairs(n-2)
        return first + second
        