class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr_summ = 0
        for n in nums:
            if curr_summ<0:
                curr_summ =0
            curr_summ += n
            maxi = max(maxi,curr_summ)
        return maxi