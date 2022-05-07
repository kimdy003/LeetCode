class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            
            if idx >= len(nums2) - 1:
                ans.append(-1)
                continue
            
            Max = nums2[idx]
            for n in nums2[idx + 1 :]:
                if Max < n:
                    ans.append(n)
                    break
            else:
                ans.append(-1)
        
        return ans