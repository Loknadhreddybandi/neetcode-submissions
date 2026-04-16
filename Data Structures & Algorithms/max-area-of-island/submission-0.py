class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0
        def bfs(row,col):
            
            queue = collections.deque()
            queue.append((row,col))
            visit.add((row,col))
            area = 1
            while queue:
                row,col = queue.popleft()
                directions = [[0,1],[-1,0],[1,0],[0,-1]]
                for dr,dc in directions:
                    r = row+dr
                    c = col + dc
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==1 and (r,c) not in visit:
                        queue.append((r,c))
                        visit.add((r,c))

                        area +=1
            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1and (row,col) not in visit:
                    max_area = max(max_area, bfs(row, col))
        return max_area
                        


        