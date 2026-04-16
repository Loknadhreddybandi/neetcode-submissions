class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nse(heights):
            n = len(heights)
            res = [n] * n        # default n means no smaller found, use n as right boundary
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    res[idx] = i
                stack.append(i)
            return res

        def pse(heights):
            n = len(heights)
            res = [-1] * n       # default -1 means no smaller found, use -1 as left boundary
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res


        n = len(heights)
        next_smaller = nse(heights)
        prev_smaller = pse(heights)
        
        maxArea = 0
        for i in range(n):
            height = heights[i]
            width = next_smaller[i] - prev_smaller[i] - 1
            maxArea = max(maxArea, height * width)
        
        return maxArea
        