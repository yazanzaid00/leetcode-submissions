# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        node_1, node_2 = list1, list2
        tail = head = list1 if list1.val <= list2.val else list2
        while node_1 and node_2:
            if node_1.val <= node_2.val:
                tail.next, node_1 = node_1, node_1.next
            else:
                tail.next, node_2 = node_2, node_2.next
            tail = tail.next
        tail.next = node_1 or node_2
        return head