class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        if sum(nums) % 2 !=0:
            return False
        def dfs(index,target):
            if index >= len(nums):
                return False
            if target ==0:
                return True
            if target<0:
                return False
            if (index,target) in memo:
                return memo[(index,target)]
            skip = dfs(index+1,target)
        

            take =  dfs(index+1,target - nums[index])
            memo[(index,target)] = skip or take
            return memo[(index,target)]
        return dfs(0,sum(nums)//2)
            


        