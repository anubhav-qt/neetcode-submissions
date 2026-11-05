class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, res = 0, ""

        def longest_from_mid(left: int, right: int) -> (int, int):
            """Returns the left and right indices of the longest palindrome from the particular mid"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return (left + 1, right - 1)

        for mid in range(len(s)):
            l1, r1 = longest_from_mid(mid, mid)
            l2, r2 = longest_from_mid(mid, mid + 1)

            if (r1 - l1) > (r2 - l2):
                curr_len = r1 - l1 + 1
                l, r = l1, r1
            else:
                curr_len = r2 - l2 + 1
                l, r = l2, r2
            
            if max_len < curr_len:
                max_len = curr_len
                res = s[l: r + 1]
        
        return res
