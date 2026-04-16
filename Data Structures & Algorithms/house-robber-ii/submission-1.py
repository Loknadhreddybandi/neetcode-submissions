class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.houserob(nums[1:]),self.houserob(nums[:-1]))
    def houserob(self,nums:List[int]):
        prev = 0
        curr = 0
        for i in range(len(nums)):
            newrob = max(prev+nums[i],curr)
            prev = curr
            curr = newrob
        return curr 
        
        