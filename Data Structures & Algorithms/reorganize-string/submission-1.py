import heapq
from collections import Counter, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = []
        for char, freq in count.items():
            heapq.heappush(maxheap, (-freq, char))  
        
        queue = deque()  
        time = 0
        result = []
        
        while maxheap or queue:
            time += 1
            
            if maxheap:
                freq, char = heapq.heappop(maxheap)
                result.append(char)
                freq += 1                            
                if freq < 0:                         
                    queue.append((time + 1, freq, char)) 
            
            if queue and queue[0][0] <= time:       
                item = queue.popleft()               
                heapq.heappush(maxheap, (item[1], item[2]))
        
        result_str = "".join(result)
        
        for i in range(1, len(result_str)):
            if result_str[i] == result_str[i-1]:
                return ""
        
        if len(result_str) == len(s):
            return result_str
            
        return  ""
        
        
        