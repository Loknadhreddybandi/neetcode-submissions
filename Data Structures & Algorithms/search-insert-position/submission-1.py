class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        
        for i in range(1,len(nums)):
            if nums[i-1]<target<nums[i]:
                return i
        if target<nums[0]:
            return 0
        return len(nums)
    
        