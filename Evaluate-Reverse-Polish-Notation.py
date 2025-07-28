import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = '+-*/'
        nums = []
        for s in tokens:
            if s in opers:
                
                b = nums.pop()
                a = nums.pop()
                r = 0
                if s == '+':
                    r = a + b
                elif s == '-':
                    r = a - b
                elif s == '*':
                    r = a*b
                else:
                    r = int(a/b)
                nums.append(r)

            else:
                nums.append(int(s))
            
        return nums[0]