class prevListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Build a separate doubly-linked list with the same values
        dummy_d = prevListNode(0)
        curr_d = dummy_d
        curr_s = head

        while curr_s:
            new_node = prevListNode(curr_s.val)
            curr_d.next = new_node
            new_node.prev = curr_d if curr_d is not dummy_d else None
            curr_d = new_node
            curr_s = curr_s.next

        head_d = dummy_d.next
        tail_d = curr_d

        # 2) Reorder the doubly-linked list using the same "take from tail" idea
        left = head_d
        right = tail_d

        while (left is not None and
               right is not None and
               left != right and
               left.next != right):

            next_left = left.next
            before_tail = right.prev

            # splice right after left
            left.next = right
            right.prev = left

            right.next = next_left
            if next_left:
                next_left.prev = right

            # detach the old tail
            if before_tail:
                before_tail.next = None

            left = next_left
            right = before_tail

        # 3) Copy reordered values back into the original singly-linked list
        curr_s = head
        curr_d = head_d

        while curr_s and curr_d:
            curr_s.val = curr_d.val
            curr_s = curr_s.next
            curr_d = curr_d.next

        return
