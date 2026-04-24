from collections import defaultdict,deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        queue = deque()
        num_of_components = 0
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def bfs(node):
            if node in visit:
                return 
            queue.append(node)
            visit.add(node)
            while queue:
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
        
        for node in range(n):
            if node not in visit:
                bfs(node)
                num_of_components +=1
        return num_of_components

        
        
        