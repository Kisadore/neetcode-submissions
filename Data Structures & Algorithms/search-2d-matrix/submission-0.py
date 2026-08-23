class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        top = 0
        bot = ROW - 1

        while top <= bot:
            currRow = (top + bot) // 2
            if target > matrix[currRow][-1]:
                top = currRow + 1
            elif target < matrix[currRow][0]:
                bot = currRow - 1
            else: 
                break
        
        if top <= bot:
            left = 0
            right = COL - 1

            while left <= right:
                mid = (left + right ) // 2
                if target > matrix[currRow][mid]:
                    left = mid + 1
                elif target < matrix[currRow][mid]:
                    right = mid - 1
                else:
                    return True
        return False
