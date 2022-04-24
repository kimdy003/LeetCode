class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        temp = []
        minCost = 0
        for A, B in costs:
            temp.append(B - A)
            minCost += A
        
        temp.sort()
        for i in range(N):
            minCost += temp[i]
        return minCost
        