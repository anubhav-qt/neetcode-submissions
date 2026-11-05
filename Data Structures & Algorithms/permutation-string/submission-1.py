from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter()
        l = 0

        if len(s1) > len(s2):
            return False

        # making the first window
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        # checking if the first window itself is the permutation
        if s1_count == window_count:
            return True

        # sliding the window
        for r in range(len(s1), len(s2)):
            window_count[s2[l]] -= 1
            l += 1
            window_count[s2[r]] += 1

            if s1_count == window_count:
                return True

        return False
