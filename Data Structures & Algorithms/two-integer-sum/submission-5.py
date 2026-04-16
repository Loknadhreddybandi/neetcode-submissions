class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp  = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mpp:
                return [mpp[diff],i]
            mpp[nums[i]]=i


        
        



        
        