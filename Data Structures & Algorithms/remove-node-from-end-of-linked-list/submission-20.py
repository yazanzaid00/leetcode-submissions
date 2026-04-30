# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = 0
        dummy = ListNode(-1, head)
        n_node, curr_node = dummy, dummy
        while curr_node:
            if diff >= n:
                prev = n_node
                n_node = n_node.next
            curr_node = curr_node.next
            diff += 1
        prev.next = n_node.next
        return dummy.next