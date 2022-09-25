class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sort : O(nlogn)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        
        # set : O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        # Negative Marking : O(n)
        # 해당 값을 음수값으로 바꾸는것으로 한번 접근을 했다고 표시
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]
            
            #Resotre numbers : 지금은 필요없음
            for i in range(len(nums)):
                nums[i] = abs(nums[i])
            
            return duplicate