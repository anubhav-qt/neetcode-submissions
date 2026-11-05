class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def palindrome_from_mid(l: int, r: int) -> None:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l, r = l - 1, r + 1

        for mid in range(len(s)):
            palindrome_from_mid(mid, mid)
            palindrome_from_mid(mid, mid + 1)

        return self.res
