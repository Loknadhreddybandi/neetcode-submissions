import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))

        # (cost, node, stops)
        heap = [(0, src, 0)]

        # Track best stops to reach node
        stops = [float('inf')] * n

        while heap:
            cost, node, step = heapq.heappop(heap)

            if node == dst:
                return cost

            if step > k or step > stops[node]:
                continue

            stops[node] = step

            for nei, price in adj[node]:
                heapq.heappush(heap, (cost + price, nei, step + 1))

        return -1