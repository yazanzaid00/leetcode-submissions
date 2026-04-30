class MyQueue:

    def __init__(self):
        self._stack = []
        self._left = None
        # Keep the first element the one that is FIFO

    def push(self, x: int) -> None:
        if len(self._stack) >= 1:
            self._stack.append(x)
        else:
            self._stack.append(x)
            self._left = 0

    def pop(self) -> int:
        self._left += 1
        return self._stack[self._left - 1]

    def peek(self) -> int:
        return self._stack[self._left]

    def empty(self) -> bool:
        return self._left is None or not self._stack or len(self._stack) - self._left == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()