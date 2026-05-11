class MinStack:

    def __init__(self):
        self._stack = [] # [(1, 1), (2, 1) , (3, 1), (0, 0)]

    def push(self, val: int) -> None:
        # deal with updating the minimum
        if not self._stack:
            self._stack.append((val, val))
        else:
            prev_min = self._stack[-1][1]
            cur_min = val if val < prev_min else prev_min
            self._stack.append((val, cur_min))

    def pop(self) -> None:
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]