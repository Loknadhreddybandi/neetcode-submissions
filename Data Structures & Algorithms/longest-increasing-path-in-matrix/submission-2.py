class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [[0,-1],[-1,0],[1,0],[0,1]]
        dp = [[-1] * (n) for _ in range(m)]
        def dfs(r,c):
            if dp[r][c] !=-1:
                return dp[r][c]
            length = 1
            for dr,dc in directions:
                nr = r+dr
                nc = c + dc
                if nr in range(m) and nc in range(n) and matrix[nr][nc]> matrix[r][c]:
                    length = max(length,1+dfs(nr,nc))
            dp[r][c] = length
            return length

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(dfs(i,j),result)
        return result
        