class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def dfs(index):
            if index >= len(nums):
                return 0
            if dp[index]!=-1:
                return dp[index]

            take = dfs(index+2) + nums[index]
            skip = dfs(index+1)
            dp[index] =  max(take,skip)
            return dp[index]
        return dfs(0)
        