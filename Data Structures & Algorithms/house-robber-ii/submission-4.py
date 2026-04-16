class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # case 1: rob index 0, so index n-1 is forbidden
        dp1 = [-1] * n
        def dfs1(i):
            if i >= n or i == n - 1:  # ← cant touch last house
                return 0
            if dp1[i] != -1:
                return dp1[i]
            take     = nums[i] + dfs1(i + 2)
            not_take = dfs1(i + 1)
            dp1[i]   = max(take, not_take)
            return dp1[i]
        
        # case 2: skip index 0, so index n-1 is allowed
        dp2 = [-1] * n
        def dfs2(i):
            if i >= n or i==0 :
                return 0
            if dp2[i] != -1:
                return dp2[i]
            take     = nums[i] + dfs2(i + 2)
            not_take = dfs2(i + 1)
            dp2[i]   = max(take, not_take)
            return dp2[i]
        
        return max(dfs1(0), dfs2(1))
       