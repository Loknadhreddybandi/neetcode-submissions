class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1