# two pointer solution
# l, r at left and rightmost points
# at each point, we shift the pointer having the smaller height by one
# also keeping track of max_left and max_right
# edge case: can't store any water at 0 or len - 1
# for all others, we check how much water is stored by min of max_left and max_right height and subtracting with the height[i]

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l, r = 0, length - 1
        max_left, max_right = 0, 0
        area = 0

        while l < r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])

            if height[l] <= height[r]:
                area += max(max_left - height[l], 0)
                l += 1
            else:
                area += max(max_right - height[r], 0)
                r -= 1
        
        return area
