class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, length = [], len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, length - 1
            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    temp = nums[l]
                    while l < r and nums[l] == temp:
                        l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    l += 1
            
        return res
