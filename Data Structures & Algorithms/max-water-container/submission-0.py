class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        if heights[l] < heights[r]:
            max_area = heights[l] * (r - l)
        else:
            max_area = heights[r] * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            if heights[l] < heights[r]:
                max_area = max(max_area, heights[l] * (r - l))
            else:
                max_area = max(max_area, heights[r] * (r - l))
        
        return max_area
                