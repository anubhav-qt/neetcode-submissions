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
            window_size = r - l + 1

            # while window is not valid
            while window_size - max_freq > k and l < r:
                char_map[s[l]] -= 1
                l += 1
                window_size = r - l + 1

            # update the max_length
            max_length = max(max_length, window_size)
            
        return max_length
