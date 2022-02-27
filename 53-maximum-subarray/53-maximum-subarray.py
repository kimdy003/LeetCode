class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxSum = nums[0]
        tempSum = nums[0]
        for n in nums[1:]:
            if tempSum < 0:
                tempSum = n
            else:
                tempSum += n
            
            maxSum = max(maxSum, tempSum)
        
        return maxSum
