class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        for i in range(len(nums)):
            summ = 0
            for j in range(i,len(nums)):
                summ += nums[j]
                
                maxi = max(maxi,summ)
        return maxi

        