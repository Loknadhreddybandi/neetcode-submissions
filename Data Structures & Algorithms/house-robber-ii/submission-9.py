class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo = {}
        n = len(nums)
        def dfs(index,end):
            if index>end:
                return 0
            if (index,end) in memo:
                return memo[(index,end)]
            skip = dfs(index+1,end)
            
            take = dfs(index+2,end) + nums[index]
            memo[(index,end)] =  max(take,skip)
            return memo[(index,end)]
        return max(dfs(0,n-2),dfs(1,n-1))

        