from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        queue = deque()
        for u,v in prerequisites:
            adj_list[v].append(u)
        in_degree = [0] * numCourses
        for u,v in prerequisites:
            in_degree[u]+=1
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        Valid_order = []
        while queue:
            node = queue.popleft()
            Valid_order.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        if len(Valid_order)==numCourses:
            return Valid_order
        return []
        