class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total// 2
        n = len(nums)
        
        dp = [[None] * (target + 1) for _ in range(n+1)]
        
        if total%2 !=0:
            return False
        def dfs(index,summ):
            if index >=len(nums):
                return False
            if summ ==0:
                return True
            if summ<0:
                return False
            if dp[index][summ] is not None:
                return dp[index][summ]
            skip = dfs(index+1,summ)
            take = dfs(index+1,summ-nums[index])
            dp[index][summ] =  skip or take
            return dp[index][summ]
        return dfs(0,total//2)
    
