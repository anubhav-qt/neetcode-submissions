from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        valid = set()
        res = ""
        min_length = float("inf")
        l = 0

        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] += 1
                if have[s[r]] >= need[s[r]]:
                    valid.add(s[r])
            
            if len(valid) == len(need) and r - l + 1 < min_length:
                min_length = r - l + 1
                res = s[l: r + 1]
                
            
            while l <= r and len(valid) == len(need):
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    valid.remove(s[l])
                l += 1
                if len(valid) == len(need) and r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l: r + 1]
        
        return res
