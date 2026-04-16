import heapq
from collections import Counter, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        st = Counter(s)
        maxheap = []

        for char, count in st.items():
            heapq.heappush(maxheap, (-count, char))

        queue = deque()
        time = 0
        res = []

        while maxheap or queue:
            time += 1

            if maxheap:
                count, char = heapq.heappop(maxheap)
                res.append(char)

                if count + 1 < 0:
                    queue.append((time + 1, count + 1, char))

            if queue and queue[0][0] <= time:
                _, count, char = queue.popleft()
                heapq.heappush(maxheap, (count, char))

        result = "".join(res)
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                return ""

        return result
        