from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        window_count = [0] * 26
        l = 0

        if len(s1) > len(s2):
            return False

        # making the first window
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # checking if the first window itself is the permutation
        if s1_count == window_count:
            return True

        # sliding the window
        for r in range(len(s1), len(s2)):
            window_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            window_count[ord(s2[r]) - ord('a')] += 1

            if s1_count == window_count:
                return True

        return False
