import sys
sys.setrecursionlimit(10000)
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(index):
            if index >= len(nums)-1:
                return 0
            if nums[index]==0:
                return float('inf')
            if index in memo:
                return memo[index]
            mini = float('inf')
            for i in range(1,nums[index]+1):
                mini =   min(mini,1+dfs(index+i))
            memo[index] = mini
            return memo[index]
        return dfs(0)

        