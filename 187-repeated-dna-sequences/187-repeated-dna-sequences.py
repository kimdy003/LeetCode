import collections


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = defaultdict(int)
        
        for i in range(len(s)):
            seq[s[i:i+10]] += 1
        
        return [key for key, value in seq.items() if value > 1]