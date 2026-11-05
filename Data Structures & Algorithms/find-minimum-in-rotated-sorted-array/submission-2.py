class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if the array is already sorted or when we reach the sorted part having the minimum value
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]: # the left part doesn't have the minimum
                l = mid + 1
            else:
                r = mid - 1

        return res
