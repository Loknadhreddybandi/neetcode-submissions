class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        stack = []
        num_of_components = 0
        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        for i in range(n):
            if i not in visit:
                visit.add(i)
                stack.append(i)
                while stack:
                    node = stack.pop()
                    for neighbor in adj_list[node]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            stack.append(neighbor)
                num_of_components +=1
        return num_of_components
        
        
        