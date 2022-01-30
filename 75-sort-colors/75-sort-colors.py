class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quick(nums, start, end):
            if start >= end:
                return
            
            key = start
            left, right = start + 1, end
            
            while left <= right:
                while left <= end and nums[left] <= nums[start]:
                    left += 1
                while start < right and nums[right] >= nums[key]:
                    right -= 1
                
                if left < right:
                    nums[right], nums[left] = nums[left], nums[right]
                else:
                    nums[key], nums[right] = nums[right], nums[key]
                

            quick(nums, start, right-1)
            quick(nums, right + 1, end)
        
        quick(nums, 0, len(nums)-1)
    
        return(nums)