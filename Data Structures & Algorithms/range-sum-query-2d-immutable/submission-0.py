class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]: return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Exact same size as input
        self.pref = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                top = self.pref[r-1][c] if r > 0 else 0
                left = self.pref[r][c-1] if c > 0 else 0
                top_left = self.pref[r-1][c-1] if (r > 0 and c > 0) else 0
                
                # Formula: Current + Top + Left - TopLeft
                self.pref[r][c] = matrix[r][c] + top + left - top_left

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        bottom_right = self.pref[r2][c2]
        
        # We need the values JUST OUTSIDE the boundaries r1 and c1
        top = self.pref[r1-1][c2] if r1 > 0 else 0
        left = self.pref[r2][c1-1] if c1 > 0 else 0
        top_left = self.pref[r1-1][c1-1] if (r1 > 0 and c1 > 0) else 0
        
        # Formula: BigBox - TopBox - LeftBox + Overlap
        return bottom_right - top - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)