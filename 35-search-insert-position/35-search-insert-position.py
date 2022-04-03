class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        
        for i, k in enumerate(nums, 1):
            if k < target:
                ans = i
            else:
                break
        
        return ans