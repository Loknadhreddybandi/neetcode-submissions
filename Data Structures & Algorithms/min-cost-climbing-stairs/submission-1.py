class Solution:
    def mincost(self,index,cost,dp):
        if index ==0 :
            return cost[index]
        if index ==1:
            return cost[index]
        if dp[index]!=-1:
            return dp[index]
        step1 =self.mincost(index-1,cost,dp)+cost[index]
        step2 = self.mincost(index-2,cost,dp)+cost[index]
        dp[index] =  min(step1,step2) 
        return dp[index]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp =[-1]*n
        return min(self.mincost(n-1,cost,dp),self.mincost(n-2,cost,dp))

        