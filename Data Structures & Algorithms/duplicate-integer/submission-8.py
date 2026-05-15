
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            dct[num] = 1+dct.get(num,0)
        for key,value in dct.items():
            if value > 1:
                return True
        return False
        