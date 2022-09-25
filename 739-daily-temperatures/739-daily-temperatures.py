class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        
        for cur, cur_tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_tmp:
                ans[stack[-1]] = cur - stack[-1]
                stack.pop()
            stack.append(cur)
        
        return ans
        