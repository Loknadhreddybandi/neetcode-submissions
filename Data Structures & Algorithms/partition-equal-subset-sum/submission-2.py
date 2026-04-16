class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}
        if total%2 !=0:
            return False
        def dfs(index,summ):
            if index >=len(nums):
                return False
            if summ ==0:
                return True
            if summ<0:
                return False
            if (index,summ) in memo:
                return memo[(index,summ)]
            skip = dfs(index+1,summ)
            take = dfs(index+1,summ-nums[index])
            memo[(index,summ)] =  skip or take
            return memo[(index,summ)]
        return dfs(0,total//2)
    
