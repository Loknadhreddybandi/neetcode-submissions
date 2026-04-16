class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def bfs(row,col):
            queue = collections.deque()
            queue.append((row,col))
            visit.add((row,col))
            while queue:
                row,col = queue.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=='1'and (r,c)not in visit:
                        queue.append((r,c))
                        visit.add((r,c))

            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and (row,col) not in visit:
                    bfs(row,col)
                    islands +=1
        return islands



        