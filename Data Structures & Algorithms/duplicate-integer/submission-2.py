class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            count = dct.get(num,0) # retrives the value associated with key
            dct[num] = count + 1
        for k,v in dct.items():
            if v>1:
                return True
        return False

        