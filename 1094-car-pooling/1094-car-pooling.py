class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1001

        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]

        cnt = 0
        for passenger in passengers:
            cnt += passenger

            if cnt < 0 or cnt > capacity:
                return False
        return True