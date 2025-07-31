class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x  # Handle edge cases
        
        left, right = 1, x // 2  # Narrow search range
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < x:
                left = mid + 1
            elif square > x:
                right = mid - 1
            elif square == x:
                return mid

        return right