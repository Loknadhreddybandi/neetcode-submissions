import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_n = {}
        for i in range(len(nums)):
            count_n[nums[i]] = 1+count_n.get(nums[i],0)
        min_heap = []
        for key,value in count_n.items():
            heapq.heappush(min_heap,(value,key))
            
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result = []
        for freq,num in min_heap:
            result.append(num)
        return result


        