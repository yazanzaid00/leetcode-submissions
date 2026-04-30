import heapq
from collections import defaultdict

class MinStack:

    def __init__(self):
        self._stack = []
        self._min_heap = []
        self._counter = defaultdict(int)

    def push(self, val: int) -> None:
        self._stack.append(val)
        heapq.heappush(self._min_heap, val)
        self._counter[val] += 1

    def pop(self) -> None:
        val = self._stack.pop()
        self._counter[val] -= 1
        if self._counter[val] == 0:
            del self._counter[val]
        return val  # not required by the API, but kept to preserve your structure

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        # Lazy deletion: only remove stale elements from the heap *root*.
        while self._min_heap and self._min_heap[0] not in self._counter:
            heapq.heappop(self._min_heap)
        return self._min_heap[0]