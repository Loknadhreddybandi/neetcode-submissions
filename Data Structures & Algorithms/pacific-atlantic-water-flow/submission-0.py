class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        

        def dfs(r,c,visit,prevheights):
            if (r<0 or r==rows or c<0 or c==cols or heights[r][c]<prevheights or (r,c) in visit):
                return 
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc,visit,heights[r][c])




        for c in range(cols): # top and bottom are fixed
            dfs(0,c,pacific,heights[0][c]) #top
            dfs(rows-1,c,atlantic,heights[rows-1][c]) #bottom
        
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0]) #left
            dfs(r,cols-1,atlantic,heights[r][cols-1]) #right

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result

        