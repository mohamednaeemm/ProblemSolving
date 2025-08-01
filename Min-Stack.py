class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.front = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.front == - 1:
            self.minStack.append(val)
        else:
            minVal = min(self.minStack[self.front], val)
            self.minStack.append(minVal)

        self.front += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.front -= 1

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()