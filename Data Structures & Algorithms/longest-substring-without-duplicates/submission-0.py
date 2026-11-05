# sliding window with a set solution
# we start with l, r = 0, 0
# iterate through the string
# when we see a char, we add it in the seen set
# then when we go to the next char, if it is already in the seen set then we iteratively remove all the characters from the left till we remove the seen character (also removing the removed characters from the seen set)
# after every iteration, we check the max_length and the current length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        seen = set()

        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(max_length, (r - l) + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        
        return max_length
