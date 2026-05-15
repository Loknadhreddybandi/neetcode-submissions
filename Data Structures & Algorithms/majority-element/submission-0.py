class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1+hashmap.get(num,0)
        for key,value in hashmap.items():
            if value > len(nums)//2:
                return key