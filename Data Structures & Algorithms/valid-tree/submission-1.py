class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visit = set()
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        def detect_cycle(node,parent):
            visit.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent :
                    continue
                if neighbor in visit:
                    return True
                if detect_cycle(neighbor,node):
                    return True
                
            return False
        if detect_cycle(0,-1):
            return False
        return len(visit)==n
        