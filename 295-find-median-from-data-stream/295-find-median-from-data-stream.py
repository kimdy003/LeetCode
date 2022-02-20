from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.bot = []
        self.top = []

    def addNum(self, num: int) -> None:
        heappush(self.bot, -num)
        heappush(self.top, -heappop(self.bot))
        
        # top의 길이는 항상 bot의 길이보다 작거나 같아야한다.
        if len(self.bot) < len(self.top):
            heappush(self.bot, -heappop(self.top))
            
    def findMedian(self) -> float:
        if len(self.top) < len(self.bot):
            return -self.bot[0]
        else:
            return (self.top[0] - self.bot[0]) / 2