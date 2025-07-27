class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue/peek

    def push(self, x: int) -> None:
        self.stack1.append(x)  # Push to stack1 (O(1))

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Transfer to stack2 (O(1) per pop)
        if not self.stack2:
            raise Exception("Queue is empty")
        return self.stack2.pop()  # Pop from stack2 (O(1))

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise Exception("Queue is empty")
        return self.stack2[-1]  # View top of stack2 (O(1))

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

# Example usage:
# queue = MyQueue()
# queue.enqueue(1)
# queue.enqueue(2)
# print(queue.peek())    # Output: 1
# print(queue.dequeue()) # Output: 1
# print(queue.dequeue()) # Output: 2
# print(queue.empty())   # Output: True