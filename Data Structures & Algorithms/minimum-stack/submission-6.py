class MinStack:

    def __init__(self):
        # 1, 2, 3, -2, -3
        self._stack = []

    def push(self, val: int) -> None:
        min_val = min(val, self._stack[-1][1]) if self._stack else val
        self._stack.append((val, min_val))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]
        

    def getMin(self) -> int:
        return self._stack[-1][1]