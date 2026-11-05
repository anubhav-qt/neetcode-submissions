from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # value, index
        res = []
        
        # sliding window algorithm
        for i in range(len(nums)):
            while dq and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append([nums[i], i])
            if i >= k - 1:
                while dq[0][1] < i - k + 1:
                    dq.popleft()
                res.append(dq[0][0])
        
        return res
