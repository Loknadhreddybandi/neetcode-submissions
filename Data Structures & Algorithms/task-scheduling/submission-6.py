import heapq
from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = []
        for char, freq in count.items():
            heapq.heappush(maxheap, (-freq, char))
        
        queue = deque()  # (available_time, count, char)
        time = 0
        
        while maxheap or queue:
            time += 1
            
            if maxheap:
                freq, char = heapq.heappop(maxheap)
                if freq + 1 < 0:
                    queue.append((time + n, freq + 1, char))  # ← only change
            
            if queue and queue[0][0] <= time:
                _, freq, char = queue.popleft()
                heapq.heappush(maxheap, (freq, char))
        
        return time

        
        
        