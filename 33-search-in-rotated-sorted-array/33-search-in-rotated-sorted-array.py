class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums.count(target) == 0:
            return -1
        
        else:
            return nums.index(target)