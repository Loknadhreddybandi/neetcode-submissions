from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for key,value in sorted(counter.items()):
            if value > len(nums)/3:
                result.append(key)
        return result