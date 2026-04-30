class MyStack:

    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue_1) - 1):
            self.queue_2.append(self.queue_1.popleft())
        val = self.queue_1.popleft()
        self.queue_1 = self.queue_2
        return val

    def top(self) -> int:
        for i in range(len(self.queue_1)):
            val = self.queue_1.popleft()
            self.queue_2.append(val)
            
        self.queue_1 = self.queue_2
        return val
        

    def empty(self) -> bool:
        return len(self.queue_1) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()