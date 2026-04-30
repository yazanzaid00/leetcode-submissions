class MinStack:
    def __init__(self):
        self.stack = []  # each element: (value, min_so_far)

    def push(self, val: int) -> None:
        # Compute min_so_far from either this value or the previous min
        if not self.stack:
            curr_min = val
        else:
            curr_min = min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        # Problem guarantees pop() is only called on non-empty stacks
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
