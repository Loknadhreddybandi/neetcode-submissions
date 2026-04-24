class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[-1,0],[0,-1],[1,0]]

        def dfs(r, c):
            if (r<0 or r==rows or c<0 or c==cols or 
                board[r][c] != 'O'):
                return
            board[r][c] = 'S'           # connected to border → safe
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # step 1 - border O's → mark S
        for c in range(cols):
            dfs(0, c)           # top
            dfs(rows-1, c)      # bottom
        
        for r in range(rows):
            dfs(r, 0)           # left
            dfs(r, cols-1)      # right

        # step 2 - flip
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':    # not connected to border → flip X
                    board[r][c] = 'X'
                elif board[r][c] == 'S':  # connected to border → restore O
                    board[r][c] = 'O'
                # X → untouched
        