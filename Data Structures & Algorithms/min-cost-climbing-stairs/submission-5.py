from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def recursive(index):
            if index >= len(cost):
                return 0
            return cost[index] + min(recursive(index+1), recursive(index+2))
        
        return min(recursive(0), recursive(1))
            
        

        