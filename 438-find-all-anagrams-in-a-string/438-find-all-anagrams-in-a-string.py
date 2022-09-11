from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        myDictP = Counter(p)
        myDictS = Counter(s[:len(p)])
        ans=[]
        left, right = 0, len(p)
        
        while right<=len(s):
            if myDictS == myDictP:
                ans.append(left)

            myDictS[s[left]]-=1
            if myDictS[s[left]]<=0:
                myDictS.pop(s[left])
                
            if right<len(s):    
                 myDictS[s[right]]+=1
                    
            left += 1
            right += 1
            
        return ans