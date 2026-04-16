import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)


        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        n = len(self.minheap)
        for i in range(n-self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
