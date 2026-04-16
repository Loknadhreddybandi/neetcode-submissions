from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        adj_list = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[u].append(v)
        in_degree = [0] * numCourses
        for u , v in prerequisites:
            in_degree [v] +=1
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        order_ = []
        while queue:
            node = queue.popleft()
            order_.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor] -=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        if len(order_)==numCourses:
            return True
        return False
            
        