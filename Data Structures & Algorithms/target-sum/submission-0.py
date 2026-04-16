class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(index,t):

            if index ==len(nums):
                if t ==0:
                    return 1
                else:
                    return 0
            if (index,t) in memo:
                return memo[(index,t)]
            summ = dfs(index +1, t-nums[index])
            subb = dfs(index +1 , t + nums[index]) # thid dfs call leads to t negative we need to add this to get 0
            memo[(index,t)] =  summ + subb
            return  memo[(index,t)]
        return dfs(0,target)