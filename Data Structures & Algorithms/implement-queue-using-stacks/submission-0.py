class MyQueue:

    def __init__(self):
        self.stack = []
        self.left = 0
        self.right = 0
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.right += 1
        

    def pop(self) -> int:
        if self.left >= self.right:
            return None
        self.left += 1
        return self.stack[self.left - 1]
        

    def peek(self) -> int:
        if self.left < self.right:
            return self.stack[self.left]
        else:
            return None

    def empty(self) -> bool:
        return self.left >= self.right


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()