class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow = 0
        botRow = len(matrix) - 1

        while topRow <= botRow:
            midRow = (topRow + botRow) // 2
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                botRow = midRow - 1
            else:
                break
        
        if topRow > botRow:
            return False

        l = 0
        r = len(matrix[0])
        while l <= r:
            m = (l + r) // 2
            if target == matrix[midRow][m]:
                return True
            elif target < matrix[midRow][m]:
                r = m - 1
            else:
                l = m + 1
        
        return False


        