from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(deque)

        for start, end in sorted(tickets):
            dic[start].append(end)

        lst = []

        def DFS(node):
            while dic[node]:
                DFS(dic[node].popleft())
            lst.append(node)

        DFS("JFK")
        return lst[::-1]