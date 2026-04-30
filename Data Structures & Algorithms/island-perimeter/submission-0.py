class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        shared = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    perimeter+=4
                    #right we are at same row and col is j+1
                    if j+1<len(grid[0]) and grid[i][j+1] == 1:
                        shared +=1
                    #bottom 
                    if i+1<len(grid) and grid[i+1][j] ==1:
                        shared +=1
        return perimeter - (2*shared)
                    
        