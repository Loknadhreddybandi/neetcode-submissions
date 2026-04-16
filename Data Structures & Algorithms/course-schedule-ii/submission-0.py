from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        # create an adjacency list 
        adj_list = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)
        in_degree = [0]*numCourses
        for a , b in prerequisites:
            in_degree[a]+=1
        # loop through numCourses and figure out courses that donot have any prerequisites
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor] -=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        if len(topo_sort) == numCourses:
            return topo_sort
        return []
        