import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u,v,cost in flights:
            adj_list[u].append((v,cost))
        dist = [float('inf')] * (n)
        dist[src] = 0
        min_heap = []
        heapq.heappush(min_heap, (0, src, k+1))
        while min_heap:
            cost,node,stops = heapq.heappop(min_heap)
            if node == dst:
                return cost
            if stops ==0:
                continue
            for neighbor,c in adj_list[node]:
                new_cost = cost  + c
                heapq.heappush(min_heap,(new_cost,neighbor,stops-1))
        return -1

        