class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):
            if i<0 or i==rows or j<0 or j==cols:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==rows-1 and j==cols-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            right = dfs(i,j+1)
            down = dfs(i+1,j)
            memo[(i,j)] =  right + down
            return memo[(i,j)]
        return dfs(0,0)
            

        