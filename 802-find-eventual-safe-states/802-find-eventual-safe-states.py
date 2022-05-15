class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def DFS(node):
            for child in graph[node]:
                if child in visit:
                    return False
                if child in ans:
                    continue
                
                visit.add(child)
                if not DFS(child):
                    return False
                visit.remove(child)
            ans.add(node)
            return True

        ans = set()
        for i in range(len(graph)):
            visit = set([i])
            DFS(i)
  
                
        return sorted(list(ans))