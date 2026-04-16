from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        counter = Counter(nums)
        for key,value in counter.items():
            heapq.heappush(min_heap,(value,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result = []
        for freq,key in min_heap:
            result.append(key)
        return result
        
        