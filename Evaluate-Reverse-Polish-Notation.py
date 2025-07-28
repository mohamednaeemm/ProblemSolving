class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Local stack to avoid persistent state
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                if len(stack) < 2:  # Check for sufficient operands
                    raise ValueError("Invalid RPN expression")
                b = stack.pop()  # Second operand (last pushed)
                a = stack.pop()  # First operand
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Truncate toward zero for division
                    stack.append(int(a / b))  # int() truncates toward zero
            else:
                stack.append(int(token))  # Convert string to integer
        if len(stack) != 1:  # Ensure exactly one result
            raise ValueError("Invalid RPN expression")
        return stack[-1]

# Example usage:
# sol = Solution()
# print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
# print(sol.evalRPN(["4", "13", "5", "/", "+"])) # Output: 6
# print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) # Output: 22