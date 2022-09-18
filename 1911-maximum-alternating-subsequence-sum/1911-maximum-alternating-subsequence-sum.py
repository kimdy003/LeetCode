class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = even = 0
        
        for n in nums:
            odd, even = max(odd, even - n), max(even, odd + n)
        

        return even