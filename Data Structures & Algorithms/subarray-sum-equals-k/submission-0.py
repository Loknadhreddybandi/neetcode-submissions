class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1} # i have seen a sum 0 once
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            needed = prefix - k 
            if needed in hashmap:
                count += hashmap[needed]
            hashmap[prefix] = 1 + hashmap.get(prefix,0)
        return count
        




        