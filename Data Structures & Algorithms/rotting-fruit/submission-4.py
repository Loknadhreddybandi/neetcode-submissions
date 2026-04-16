class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        fresh = 0
        minutes = 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:          # no duplicate check needed
                    visit.add((r, c))
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:                        # edge case
            return 0

        def bfs():
            nonlocal fresh
            nonlocal minutes
            directions = [[0,-1],[1,0],[0,1],[-1,0]]
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(rows) and c in range(cols)
                            and grid[r][c] == 1
                            and (r,c) not in visit):
                            visit.add((r, c))
                            queue.append((r, c))
                            fresh -= 1
                minutes += 1

            if fresh != 0:
                return -1
            return minutes - 1

        return bfs()

        