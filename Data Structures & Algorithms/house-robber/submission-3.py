from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(index):
            if index >=len(nums):
                return 0 # last elemnt to rob is at last index
            take = nums[index] + dfs(index+2) #skip next to that index so we can rob safely
            nottake = dfs(index+1)
            return max(nottake,take)
        return dfs(0)
       
        
       