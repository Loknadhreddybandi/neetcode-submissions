class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            a = nums[i]
            nums_needed = target - a
            if nums_needed in map:
                return [map[nums_needed],i]
            map[a] = i
        return []
        