from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_length = 0, 0
        char_map = defaultdict(int) # char: frequency (in the current window)
        max_freq = 0

        for r in range(len(s)):
            # add the right char in the window
            char_map[s[r]] += 1
            max_freq = max(max_freq, char_map[s[r]])

            # while window is not valid
            while (r - l + 1) - max_freq > k:
                char_map[s[l]] -= 1
                l += 1

            # update the max_length
            max_length = max(max_length, r - l + 1)
            
        return max_length
