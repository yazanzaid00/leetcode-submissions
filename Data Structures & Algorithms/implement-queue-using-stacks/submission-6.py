class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.first_node = None
        self.left, self.right = 0, 0

    def push(self, x: int) -> None:
        node = Node(x, None)
        if self.empty() :
            self.first_node = node
        else:
            self.stack_1[-1].next_node = node
        self.stack_1.append(node)
        self.right += 1


    def pop(self) -> int:
        if self.empty():
            return None
        val = self.first_node.val
        self.first_node = self.first_node.next_node
        self.left += 1
        return val

    def peek(self) -> int:
        return None if self.empty() else self.first_node.val

    def empty(self) -> bool:
        return not self.stack_1 or not self.first_node or self.left >= self.right


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()