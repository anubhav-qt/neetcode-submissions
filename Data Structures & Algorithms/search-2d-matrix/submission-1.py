class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_out, r_out = 0, len(matrix) - 1

        while l_out <= r_out:
            l_in, r_in = 0, len(matrix[0]) - 1
            mid_out = l_out + ((r_out - l_out) // 2)

            if matrix[mid_out][l_in] <= target and matrix[mid_out][r_in] >= target:
                while l_in <= r_in:
                    mid_in = l_in + ((r_in - l_in) // 2)

                    if matrix[mid_out][mid_in] == target:
                        return True
                    elif matrix[mid_out][mid_in] < target:
                        l_in = mid_in + 1
                    else:
                        r_in = mid_in - 1
                
                return False
            
            elif matrix[mid_out][l_in] < target:
                l_out = mid_out + 1
            
            else:
                r_out = mid_out - 1
            
        return False
