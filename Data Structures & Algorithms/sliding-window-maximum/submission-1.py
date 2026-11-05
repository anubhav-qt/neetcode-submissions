from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # value, index
        res = []

        # filling the window for the first time
        for i in range(k):
            while dq and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append([nums[i], i])
        res.append(dq[0][0])
        
        # the algorithm
        for i in range(k, len(nums)):
            while dq and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append([nums[i], i])
            while dq[0][1] < abs(i - k) + 1:
                dq.popleft()
            res.append(dq[0][0])
        
        return res
