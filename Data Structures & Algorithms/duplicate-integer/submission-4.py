from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = 1+dct.get(nums[i],0)

        for k,v in dct.items():
            if v >1 :
                return True
        return False

        