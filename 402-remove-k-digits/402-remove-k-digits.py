class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        while stack and k:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        return str(int(''.join(stack)))