"""
find the index of the minimum element, then binary search in the correct section for the answer.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding the index of the minimum element in O(log n)
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        # finding the element in O(log n)
        if target >= nums[min_index] and target <= nums[-1]:
            r = len(nums) - 1
        else:
            l = 0
            r = min_index - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
