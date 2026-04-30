# Definition for singly-linked list.
# LeetCode already provides this class.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional['ListNode']) -> None:
        """
        Reorders the list in-place from:
            L0 → L1 → … → Ln-1
        to:
            L0 → Ln-1 → L1 → Ln-2 → L2 → ...
        Modifies the list and returns None.
        """

        # Edge cases: 0 or 1 node – nothing to do.
        if not head or not head.next:
            return

        # 1) Find the middle of the list using slow/fast pointers.
        #    After this loop, 'slow' will be at the end of the first half.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now:
        # head ... slow -> slow.next ... end
        # We split into two lists:
        #   first: head ... slow
        #   second: slow.next ... end
        second = slow.next
        slow.next = None  # terminate first half

        # 2) Reverse the second half in-place.
        prev = None
        curr = second
        while curr:
            nxt = curr.next      # save next
            curr.next = prev     # reverse pointer
            prev = curr          # move prev forward
            curr = nxt           # move curr forward

        # After reversing:
        # 'prev' is the head of the reversed second half.
        second = prev

        # 3) Merge the two halves, alternating nodes:
        #    first node from 'first', then one from 'second', etc.
        first = head
        while second:
            # Save next pointers before we overwrite them
            tmp1 = first.next
            tmp2 = second.next

            # Insert 'second' node after 'first'
            first.next = second
            second.next = tmp1

            # Advance both pointers
            first = tmp1
            second = tmp2

        # No explicit return; list is modified in-place.
