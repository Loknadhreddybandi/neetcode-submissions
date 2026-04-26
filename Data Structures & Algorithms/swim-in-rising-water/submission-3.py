import heapq
class Solution:
    def swimInWater(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = matrix[0][0]
        heap = []
        heapq.heappush(heap,(matrix[0][0],0,0))
        while heap:
            time,row,col = heapq.heappop(heap)
            if time > dist[row][col]:
                continue
            if row == rows-1 and col == cols-1:
                return time
            for dr,dc in directions:
                nr=row+dr
                nc = col + dc
                if (nr in range(rows) and (nc in range(cols))):
                    new_time = max(time,matrix[nr][nc])
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(heap,(new_time,nr,nc))
        return dist[rows-1][cols-1]
            
