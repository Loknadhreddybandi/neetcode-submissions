class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}
        def dfs(i,j):
            if i<0 or i==rows or j<0 or j==cols:
                return float('inf')
            if i==rows-1 and j==cols-1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            down = dfs(i+1,j)
            right = dfs(i,j+1)
            memo[(i,j)]  = grid[i][j] + min(down,right)
            return memo[(i,j)]
        return dfs(0,0)
        