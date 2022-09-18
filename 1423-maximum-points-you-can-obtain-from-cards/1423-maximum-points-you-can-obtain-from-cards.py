class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints) - k
        curr = noCard = sum(cardPoints[:N])
        
        for i in range(len(cardPoints) - N):
            curr += cardPoints[N + i] - cardPoints[i]
            noCard = min(curr, noCard)
        
        return sum(cardPoints) - noCard