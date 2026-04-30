class MinStack:

    def __init__(self):
        self._stack = list()

    def push(self, val: int) -> None:
        min_val = min(val, self._stack[-1][0]) if self._stack else val
        self._stack.append((min_val, val))

    def pop(self) -> None:
        self._stack.pop()
        
    def top(self) -> int:
        return self._stack[-1][1]
        

    def getMin(self) -> int:
        return self._stack[-1][0]