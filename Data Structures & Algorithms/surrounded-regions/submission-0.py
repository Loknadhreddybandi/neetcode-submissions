from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        rows, cols = len(board), len(board[0])
        queue = deque()

        # 1. Identify all "Safe" 'O's on the borders
        for r in range(rows):
            for c in range(cols):
                # If it's on the border and it's an 'O'
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    queue.append((r, c))
                    board[r][c] = 'S' # Mark as Safe

        # 2. Standard BFS to find all 'O's connected to the border
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    queue.append((nr, nc))

        # 3. Final Swap (The "Logic" step)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O': 
                    board[r][c] = 'X' # Was surrounded
                elif board[r][c] == 'S': 
                    board[r][c] = 'O'
            