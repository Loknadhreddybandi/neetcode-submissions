class Solution:
    def mincost(self,index,cost):
        if index ==0 :
            return cost[index]
        if index ==1:
            return cost[index]
        step1 =self.mincost(index-1,cost)+cost[index]
        step2 = self.mincost(index-2,cost)+cost[index]
        return min(step1,step2) 
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.mincost(n-1,cost),self.mincost(n-2,cost))

        