class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                temp, ttemp = s[left:right], s[left + 1 : right + 1]
                return temp == temp[::-1] or ttemp == ttemp[::-1]
            left, right = left + 1, right - 1
        return True