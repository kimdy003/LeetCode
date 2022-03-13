class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current += 1
                
                longest = max(longest, current)
        
        return longest