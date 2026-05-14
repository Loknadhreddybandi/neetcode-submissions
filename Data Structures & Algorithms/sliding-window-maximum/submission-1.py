from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for right in range(len(nums)):
            if queue and queue[0] < right - k + 1 : #window is in valid
                queue.popleft()
            current = nums[right]
            while queue and current > nums[queue[-1]]: #means current is larger so pop everything 
                queue.pop()
            queue.append(right)
            if right + 1 >=k:# bcoz where right is index
                result.append(nums[queue[0]])
        return result 
        
        

        