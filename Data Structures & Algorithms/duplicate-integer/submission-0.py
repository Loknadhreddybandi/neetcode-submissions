from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_count = Counter(nums)
        for _,value in freq_count.items():
            if value>1:
                return True
        return False
        
         