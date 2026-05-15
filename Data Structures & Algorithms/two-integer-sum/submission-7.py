class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,value in enumerate(nums):
            need =  target - value
            if need in hashmap:
                return [hashmap[need],index]
            hashmap[value] = index


            