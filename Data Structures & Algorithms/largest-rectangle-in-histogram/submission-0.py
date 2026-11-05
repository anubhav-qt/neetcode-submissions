class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while mono_stack and mono_stack[-1][1] > h:
                index, height = mono_stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            mono_stack.append((start, h))
        
        for i, h in mono_stack:
            max_area = max(max_area, h *(len(heights) - i))
        
        return max_area
