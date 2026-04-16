from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()  # (ready_time, remaining_task_count)
        maxheap = []
        s = Counter(tasks)

        for _, count in s.items():
            maxheap.append(-count)
        heapq.heapify(maxheap)

        time = 0
        while maxheap or queue:
            time += 1
            if queue and queue[0][0] == time:
                ready_time, remaining = queue.popleft()
                heapq.heappush(maxheap, remaining)

            if maxheap:
                curr = heapq.heappop(maxheap)
                if curr + 1 < 0:  # still has executions left
                    queue.append((time + n + 1, curr + 1))  # schedule with cooldown

        return time