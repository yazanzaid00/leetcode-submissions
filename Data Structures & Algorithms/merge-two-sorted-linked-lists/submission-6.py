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

        node1 = list1
        node2 = list2
        # find head
        if list1.val <= list2.val:
            tail = head = list1
            node1 = node1.next
        else:
            tail = head = list2
            node2 = node2.next
        
        while node1 and node2:
            if node1.val <= node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        tail.next = node1 or node2
        return head
