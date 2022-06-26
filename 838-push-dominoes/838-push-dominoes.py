from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        qq = deque()
        mp = {'L' : -1, 'R' : 1}
        was = [0 for _ in range(len(dominoes))]
        res = list(dominoes)
        
        for i, x in enumerate(dominoes):
            if x != '.':
                qq.append((i, 1, x))
                was[i] = -1 
        
        while qq:
            idx, depth, direction = qq.popleft()
            if 0 <= idx < len(res):
                if was[idx] == depth:
                    res[idx] = '.'
                elif was[idx] <= 0:
                    was[idx] = depth
                    qq.append((idx + mp[direction], depth + 1, direction))
                    res[idx] = direction
        
        return ''.join(res)
