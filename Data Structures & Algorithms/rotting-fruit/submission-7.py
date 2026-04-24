class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = collections.deque()
        fresh = 0
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh +=1
                elif grid[r][c]==2:
                    visit.add((r,c))
                    queue.append((r,c,0))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                row,col,dist = queue.popleft()
                for dr,dc in directions:
                    nr = row+dr
                    nc = col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh -=1
                        visit.add((nr,nc))
                        queue.append((nr,nc,dist+1))
           
        if fresh > 0:
            return -1
        return dist



        