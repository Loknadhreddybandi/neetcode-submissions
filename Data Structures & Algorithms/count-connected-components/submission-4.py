from collections import defaultdict,deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        stack = []
        num_of_components = 0
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(node):
            if node in visit:
                return
            visit.add(node) 
            stack.append(node)
            while stack:
                node = stack.pop()
                for neighbor in adj_list[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        stack.append(neighbor)
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                num_of_components +=1
        return num_of_components

        
        
        