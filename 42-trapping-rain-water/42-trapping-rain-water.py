class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0
        while left <= right:
            if height[left] <= height[right]:
                l_max = max(height[left], l_max)
                ans += l_max - height[left]
                left += 1
            else:
                r_max = max(height[right], r_max)
                ans += r_max - height[right]
                right -= 1

        return ans