# dp solution
# create max_left, max_right and min_max arrays
# then min_max[i] - height[i] for i in range(len(height))

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        min_max = [0] * length

        # fill the max_left array
        max_height = 0
        for i in range(1, length):
            max_height = max(max_height, height[i - 1])
            max_left[i] = max_height
        
        # fill the max_right array
        max_height = 0
        for i in range(length - 2, -1, -1):
            max_height = max(max_height, height[i + 1])
            max_right[i] = max_height

        # fill the min_max array and find the answer
        area = 0
        for i in range(length):
            min_max[i] = min(max_left[i], max_right[i])
            area += max(min_max[i] - height[i], 0)
        
        return area
