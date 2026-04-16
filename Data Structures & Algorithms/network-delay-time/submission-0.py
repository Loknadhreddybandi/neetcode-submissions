import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj_list[u].append((v,w))
        dist = [float('inf')] * (n + 1)
        dist[k] =0
        min_heap = []
        heapq.heappush(min_heap,(0,k))
        while min_heap : 
            d,node = heapq.heappop(min_heap)
            if d>dist[node]: #its already smaller no update
                continue
            for neighbor , time in adj_list[node]:
                new_time = dist[node] + time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap,(new_time,neighbor))
        ans = max(dist[1:]) # skip 0 index
        
        if ans != float('inf'):
            return ans
        return -1   
            

        