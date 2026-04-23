class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxarea = 0
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        def bfs(r,c):
            area = 1
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                r,c = queue.popleft()
                for row,col in directions:
                    nr = r + row
                    nc = c + col
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr,nc) not in visit):
                        visit.add((nr,nc))
                        queue.append((nr,nc))
                        area +=1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                     maxarea = max(maxarea,bfs(r,c))
        return maxarea
        