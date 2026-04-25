import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u,v,w in flights:
            adj_list[u].append((v,w))
        dist = [[float('inf')] * (n) for _ in range(n)]
        dist[src][0]=0
        heap = []
        heapq.heappush(heap,(0,src,0))
        while heap:
            cost,node,stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops>k:
                continue #skip this path
            for neighbor, cst in adj_list[node]:
                if cost + cst < dist[neighbor][stops+1]:
                    dist[neighbor][stops+1] = cost + cst
                    heapq.heappush(heap,(cost+cst,neighbor,stops+1))
        return -1


        