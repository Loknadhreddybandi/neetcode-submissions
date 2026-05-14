class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float('inf')
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target:
                minLen = min(minLen,right - left + 1)
                summ -= nums[left]
                left +=1
        if minLen != float('inf'):
            return minLen
        return 0

        