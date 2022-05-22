class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(grid), len(grid[0])        
        
        lis = sum(grid, [])
        p = len(lis) - (k % len(lis))        
        ans = lis[p:] + lis[:p]
        
        idx = 0
        for i in range(N):
            for j in range(M):
                grid[i][j] = ans[idx]
                idx += 1
        
        return grid