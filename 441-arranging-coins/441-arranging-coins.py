class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt, ans = 1, 0
        while True:
            if cnt > n:
                break
            n -= cnt
            cnt, ans = cnt + 1, ans + 1
        
        return ans
            