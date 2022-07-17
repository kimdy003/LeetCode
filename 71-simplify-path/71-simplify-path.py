class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = []
        for p in path.split("/"):
            if p in ('', '.'):
                pass
            elif p == '..':
                if lst: lst.pop()
            
            else:
                lst.append(p)

        return("/" + "/".join(lst))
