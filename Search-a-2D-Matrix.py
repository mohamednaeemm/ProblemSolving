class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        nT = len(matrix)

        m = 0
        

        while True:
            right = matrix[m][-1]
            if target <= right:
                for i in range(n):
                    if matrix[m][i] == target:
                        return True
                return False
            else:
                if m == nT - 1:
                    return False
                else:
                    m += 1
        return False