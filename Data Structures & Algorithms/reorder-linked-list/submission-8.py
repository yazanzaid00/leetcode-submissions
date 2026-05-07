# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        def reverse(node: Optional[ListNode]):
            prev, cur = None, node
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        def merge(first_list, sec_list):
            dummy = ListNode()
            head = first_list
            dummy.next = head
            first_p, second_p = first_list, sec_list
            while first_p and second_p:
                temp_first = first_p.next
                first_p.next = second_p
                
                temp_second = second_p.next
                second_p.next = temp_first

                first_p, second_p = temp_first, temp_second
            
            while head.next:
                head = head.next
            head.next = first_p or second_p
            return dummy.next



        # [0, 1, 2, 3, 4, 5, 6]
        prev = None
        fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow points to the mid of the list
        mid = slow
        prev.next = None

        rev_list = reverse(mid)

        merge(head, rev_list)


        
