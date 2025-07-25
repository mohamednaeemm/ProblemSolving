class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(left: int, right: int, s: str) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right, s) or isPalindrome(left, right - 1, s)

            left += 1
            right -= 1
        return True