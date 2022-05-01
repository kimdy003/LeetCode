class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(nums, m, mid):
                right = mid     
            else:
                left = mid + 1
        return left
    
    def feasible(self, nums: List[int], m: int, threshold: int) -> bool:
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold: # threshold보다 커지면 split한다
                total = num
                count += 1
                if count > m:  # split를 했을때 m보다 커지면 False
                    return False
        return True
        