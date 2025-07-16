class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        left = 0
        right = n -1

        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1
        
        return s
        