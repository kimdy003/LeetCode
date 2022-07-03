class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        idx = 0
        for tt in t:
            if idx == len(s):
                return True
            
            if s[idx] == tt:
                idx += 1
        
        return True if idx == len(s) else False