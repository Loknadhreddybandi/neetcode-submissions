from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        counter = Counter(nums)
        for key,value in counter.items():
            heapq.heappush(max_heap,(-value,key))
    
        result = []
        for i in range(k):
            freq,num = heapq.heappop(max_heap)
            result.append(num)
        return result
        