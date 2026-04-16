import heapq
from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        count = Counter(tasks)
        for task,task_count in count.items(): # loop through intervals and create a how many times each interval appears 
            heapq.heappush(maxheap,-task_count)
        queue = deque()
        time = 0
        while maxheap or queue:
            time +=1
            if maxheap: #we are considering one tasks so decrement the task count by 1
                task_count = 1+ heapq.heappop(maxheap)
                if task_count!=0: # if task count is 0 this means this particular task reaches its full capabality so we dont push
                    queue.append([task_count,time+n])
            if queue and queue[0][1]==time: # after decremenenting count again we can add this task as it reaches time (this means imagine there is a task with freq n so after taking one this becomes n-1 and we need to wait current_time(processed task time ) + n  so that we can take this task again)
                heapq.heappush(maxheap,queue.popleft()[0])
        return time

        
        
        