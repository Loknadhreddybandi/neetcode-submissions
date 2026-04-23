class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = collections.deque()

        # step 1 — seed all treasure chests at once
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))

        # step 2 — BFS outward from all sources in sync
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols)
                            and grid[nr][nc] == 2147483647
                            and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
                        grid[nr][nc] = dist + 1
            dist += 1
        