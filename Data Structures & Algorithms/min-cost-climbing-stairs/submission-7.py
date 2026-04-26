class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        def dfs(index):
            if index >=len(cost):
                return 0
            if dp[index]!=-1:
                return dp[index]
            step1 = dfs(index+1)
            step2 = dfs(index+2)
            dp[index] =  cost[index] + min(step1,step2)
            return dp[index]
        return  min(dfs(0),dfs(1))


        