import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        Min = math.inf
        
        for price in prices:
            Min = min(Min, price)
            Max = max(Max, price - Min)
        
        return Max