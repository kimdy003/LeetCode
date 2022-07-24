class Solution:
    def jump(self, nums: List[int]) -> int:
        next_jump = cur_jump = ans = 0
        
        for i, n in enumerate(nums[:-1]):
            next_jump = max(next_jump, i + n)
            if i == cur_jump:
                ans += 1
                cur_jump = next_jump
            
        return ans