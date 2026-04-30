# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            prev, cur = None, node
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        def merge(list1, list2, length):
            while list1 and list2:
                temp1 = list1.next
                temp2 = list2.next
                list1.next = list2
                list2.next = temp1
                list1 = temp1
                list2 = temp2


        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # reveserse the second half
        mid = length // 2
        second_half = head
        for i in range(mid + 1):
            prev = second_half
            second_half = second_half.next
        prev.next = None
        second_half = reverse(second_half)
        merge(head, second_half, length)
