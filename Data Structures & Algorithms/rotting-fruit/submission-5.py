class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = collections.deque()
        fresh = 0

        # step 1 — seed all rotten fruits, count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        # edge case — no fresh fruits at all
        if fresh == 0:
            return 0

        # step 2 — BFS outward, each level = 1 minute
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols)
                            and grid[nr][nc] == 1
                            and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
                        fresh -= 1              # one less fresh fruit
            minutes += 1

        # if fresh still > 0, some fruits were unreachable
        return minutes - 1 if fresh == 0 else -1
        