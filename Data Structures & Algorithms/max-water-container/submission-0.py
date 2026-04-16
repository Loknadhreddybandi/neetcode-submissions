class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxarea = 0
        while left<right:
            height = min(heights[left],heights[right]) # simple logic choose a one which has min height
            width = right - left # right index - left index 
            area = height * width
            maxarea = max(area,maxarea)
            #move pointers based on a condition
            if heights[left]>heights[right]:
                #choose a one with max height
                right -=1
            else:
                left +=1
        return maxarea
        