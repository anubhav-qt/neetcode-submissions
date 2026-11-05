class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l + 1) // 2

            if nums[m] > nums[r]: # this means the left half is sorted
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else: # this means the right half is sorted
                if target >= nums[m] and target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        return l if target == nums[l] else -1
