from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()  # (ready_time, count)
        maxheap = []

        s = Counter(tasks)
        for count in s.values():
            maxheap.append(-count)
        heapq.heapify(maxheap)

        time = 0
        while maxheap or queue:
            time += 1

            # Run task from heap
            if maxheap:
                curr = heapq.heappop(maxheap)
                if curr + 1 < 0:  # Task has remaining executions
                    queue.append((time + n, curr + 1))

            # Push task back to heap after cooldown
            if queue and queue[0][0] == time:
                _, task = queue.popleft()
                heapq.heappush(maxheap, task)

        return time
