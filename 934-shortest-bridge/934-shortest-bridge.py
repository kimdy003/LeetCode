from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def detect(i, j):
            grid[i][j] = -1
            q.append([i, j])
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 1:
                    detect(ny, nx)

        def frist():
            for i in range(N):
                for j in range(N):
                    if grid[i][j]:
                        return i, j

        N = len(grid)
        q = deque()
        detect(*frist())
        ans = 0

        while q:
            cnt = len(q)

            for _ in range(cnt):
                y, x = q.popleft()

                for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N:
                        if grid[ny][nx] == 1:
                            return ans
                        elif grid[ny][nx] == 0:
                            grid[ny][nx] = -1
                            q.append([ny, nx])
            ans += 1