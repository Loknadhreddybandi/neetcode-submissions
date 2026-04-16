import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = []
        current_passengers = 0
        for passengers,start,end in trips:
            while heap and heap[0][0]<=start:#this is the boarded passengers are dropped out
                _,p = heapq.heappop(heap)
                current_passengers-=p
            current_passengers += passengers
            heapq.heappush(heap,(end,passengers))
            if current_passengers>capacity:
                return False
        return True        