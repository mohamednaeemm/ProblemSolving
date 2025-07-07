class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:  # Handle empty matrix
            self.prefix_sum = []
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # Initialize prefix_sum with an extra row and column for easier computation
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Compute 2D prefix sum
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix_sum[i][j] = (
                    matrix[i-1][j-1] +                    # Current element
                    self.prefix_sum[i-1][j] +             # Sum of elements above
                    self.prefix_sum[i][j-1] -             # Sum of elements to the left
                    self.prefix_sum[i-1][j-1]             # Subtract overlap
                )
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefix_sum:  # Handle empty matrix case
            return 0
        
        # Use inclusion-exclusion to compute the sum of the rectangle
        return (
            self.prefix_sum[row2 + 1][col2 + 1] -
            self.prefix_sum[row2 + 1][col1] -
            self.prefix_sum[row1][col2 + 1] +
            self.prefix_sum[row1][col1]
        )