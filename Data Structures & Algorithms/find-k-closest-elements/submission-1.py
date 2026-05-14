import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []
        for num in arr:
            heapq.heappush(maxheap,((-abs(num - x)),- num, num))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        result = []
        for item in maxheap:
            result.append(item[2])
        return sorted(result)
        