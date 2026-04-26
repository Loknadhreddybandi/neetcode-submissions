class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def dfs(index,target):
            if index >= len(nums):
                if target==0:
                    return 1
                return 0
            if (index,target) in memo:
                return memo[(index,target)]
            
            add = dfs(index+1,target-nums[index])
            sub = dfs(index+1,target+ nums[index]) # bbcoz -(-) = +
            memo[(index,target)] = add + sub
            return memo[(index,target)]
        return dfs(0,target)