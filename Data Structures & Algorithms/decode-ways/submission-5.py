class Solution:
    def numDecodings(self, s: str) -> int:
        n0, n1 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            n = 0
            if s[i] != '0':
                n += n0
            if i + 1 < len(s) and "10" <= s[i: i + 2] <= "26":
                n += n1
            
            n0, n1 = n, n0

        return n0
