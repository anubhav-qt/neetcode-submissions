class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # A will always be the smaller array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            mid_A = l + (r - l) // 2
            mid_B = half - mid_A - 2

            A_left = A[mid_A] if mid_A >= 0 else float("-inf")
            A_right = A[mid_A + 1] if (mid_A + 1) < len(A) else float("inf")
            B_left = B[mid_B] if mid_B >= 0 else float("-inf")
            B_right = B[mid_B + 1] if (mid_B + 1) < len(B) else float("inf")

            # partitioned correctly
            if A_left <= B_right and B_left <= A_right:
                # if the total number of elements is odd
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = mid_A - 1
            else:
                l = mid_A + 1
