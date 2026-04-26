class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def dfs(index):
            if index ==n:
                return 1
            if index >n:
                return 0
            if dp[index]!=-1:
                return dp[index]

            first = dfs(index+1)
            second = dfs(index+2)
            dp[index] =  first + second
            return dp[index]
        return dfs(0)
        