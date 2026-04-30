# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        # find middle
        prev = None
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # reverse half of the linked list starting from slow
        second_list = slow.next
        slow.next = None
        prev = None
        while second_list:
            nxt = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = nxt
        # the head is at prev merge between two linked lists
        curr_1 = head
        curr_2 = prev
        while curr_1 and curr_2:
            tmp_1 = curr_1.next
            curr_1.next = curr_2
            tmp_2 = curr_2.next
            curr_2.next = tmp_1
            curr_1 = tmp_1
            curr_2 = tmp_2