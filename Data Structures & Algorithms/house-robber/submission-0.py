class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        
        def houserob(index,dp):
            if index>=len(nums):
                return 0
            if dp[index]!=-1:
                return dp[index]
            skip = houserob(index+1,dp)
            take = houserob(index+2,dp)+nums[index]
            dp[index] =  max(skip,take)
            return dp[index]
        return houserob(0,dp)
        
        