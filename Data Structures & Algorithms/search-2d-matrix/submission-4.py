class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0 
        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            if matrix[row][-1] < target:
                if row < len(matrix) - 1:
                    row += 1
                else:
                    return False

            else:
                m = (r + l) // 2
                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    r = m - 1            
        return False

            
        