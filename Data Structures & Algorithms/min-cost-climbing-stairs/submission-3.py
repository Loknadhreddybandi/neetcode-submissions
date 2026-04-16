class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        def recursive(index):
            if index >=len(cost):
                return 0
            if dp[index] !=-1:
                return dp[index]
            
            dp[index] =  cost[index] + min(recursive(index +1 ),recursive(index+2))
            return dp[index]
        return min(recursive(0),recursive(1))
        
        

        