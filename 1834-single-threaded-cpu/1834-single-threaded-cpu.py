import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        idx = 0
        hq = []
        
        time = tasks[0][0]
        
        while len(ans) < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= time:
                heapq.heappush(hq, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            
            if hq:
                process, original_idx = heapq.heappop(hq)
                time += process
                ans.append(original_idx)
            elif idx < len(tasks):
                time = tasks[idx][0]
                
        return ans
                