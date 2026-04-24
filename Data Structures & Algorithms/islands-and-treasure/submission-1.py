class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions =[[0,1],[0,-1],[1,0],[-1,0]]
        infinity = 2147483647
        visit = set()
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visit.add((r,c))
                    queue.append((r,c))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                for dr,dc in directions:
                    nr = row+dr
                    nc = col + dc
                    if (nr in range(rows) and (nc in range(cols)) and grid[nr][nc]==infinity):
                        grid[nr][nc]= dist + 1
                        visit.add((nr,nc))
                        queue.append((nr,nc))
            dist +=1

       