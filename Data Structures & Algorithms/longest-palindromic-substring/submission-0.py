class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, res = 0, ""
        
        def longest_from_center(left: int, right: int) -> (int, int):
            """Returns the left and right indices of the longest palindrome from center of a char"""
            if left < 0 and right >= len(s):
                return left + 1, right - 1

            if left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = longest_from_center(left - 1, right + 1)

            return (left, right) if ((left >= 0 and right < len(s)) and (s[left] == s[right])) else (left + 1, right - 1)
        
        for center in range(len(s)):
            # single center
            left, right = longest_from_center(center, center)
            if max_len < right - left + 1:
                max_len = right - left + 1
                res = s[left: right + 1]

            # dual center
            if center + 1 < len(s) and s[center] == s[center + 1]:
                left, right = longest_from_center(center, center + 1)
                if max_len < right - left + 1:
                    max_len = right - left + 1
                    res = s[left: right + 1]
        
        return res
