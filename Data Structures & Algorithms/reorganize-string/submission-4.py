import heapq
from collections import Counter, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = []
        result = []
        for char, freq in count.items():
            heapq.heappush(maxheap, (-freq, char))
        
        queue = deque()  # (available_time, count, char)
        time = 0
        
        while maxheap or queue:
            time += 1
            
            if maxheap:
                freq, char = heapq.heappop(maxheap)
                result.append(char)
                if freq + 1 < 0:
                    queue.append((time + 1, freq + 1, char))  # ← only change
            
            if queue and queue[0][0] <= time:
                _, freq, char = queue.popleft()
                heapq.heappush(maxheap, (freq, char))
        res = "".join(result)
        for i in range(1,len(res)):
            if res[i]==res[i-1]:
                return ""
        return res

        
       