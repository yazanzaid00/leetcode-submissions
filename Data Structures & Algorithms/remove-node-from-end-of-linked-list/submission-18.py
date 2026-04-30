# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I noticed that the n th node from the end is also len - n from the start, I need to move len - n, I can move n right pointer and then move left pointer up until n.
        right = head
        # n times
        for _ in range(n):
            right = right.next
        # len - n times
        dummy = prev = ListNode(0, head)
        left = head
        while right:
            prev, left = left, left.next
            right = right.next
        
        prev.next = left.next
        return dummy.next