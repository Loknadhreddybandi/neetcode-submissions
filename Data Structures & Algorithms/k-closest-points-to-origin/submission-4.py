import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(min_heap,(-dist,-x,-y))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        for dist,x,y in min_heap:
            result.append([-x,-y])
        return result