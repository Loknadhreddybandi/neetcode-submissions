class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        directions =[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r, c, index):
            if index == len(word):  
                return True        
            if r < 0 or r >= rows or \
            c < 0 or c >= cols:          # out of bounds
                return False
            if (r, c) in visit:             # already used
                return False
            if board[r][c] != word[index]:  # wrong char
                return False
            
            visit.add((r, c))               # mark
            
            for dr, dc in directions:
                if dfs(r+dr, c+dc, index+1):  # explore 4 directions
                    return True
            
            visit.remove((r, c))            # unmark → undo
            return False
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):            # try every cell as start
                    return True
        return False
