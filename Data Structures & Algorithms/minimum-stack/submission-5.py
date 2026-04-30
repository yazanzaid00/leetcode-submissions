class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # min_stack[i] == min(stack[0..i])

    def push(self, val: int) -> None:
        self.stack.append(val)

        # TODO: what is the "new minimum so far" after pushing val?
        # Hint: either val, or the previous min (top of min_stack).
        new_min = min(val, self.min_stack[-1]) if self.min_stack else val

        self.min_stack.append(new_min)

    def pop(self) -> None:
        # TODO: both stacks must stay perfectly aligned by size.
        # Question: what two pops must happen here?
        val = self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # TODO: return last pushed element
        return self.stack[-1]  # TODO

    def getMin(self) -> int:
        # TODO: where is the current minimum stored?
        return self.min_stack[-1]  # TODO