class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        tem = []
        minCost = 0
        for A, B in costs:
            tem.append(B - A)
            minCost += A
        
        tem.sort()
        for i in range(N):
            minCost += tem[i]
        return minCost
        