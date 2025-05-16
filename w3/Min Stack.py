class MinStack:
    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack or self.MinStack[-1] >= val:
            self.MinStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.MinStack[-1]:
            self.MinStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]