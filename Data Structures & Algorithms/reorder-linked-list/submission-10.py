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
            head = first_list
            first_p, second_p = first_list, sec_list
            while first_p and second_p:
                temp_first = first_p.next
                temp_second = second_p.next

                first_p.next = second_p
                if temp_first: # Added check to ensure the chain continues correctly
                    second_p.next = temp_first

                first_p, second_p = temp_first, temp_second
                
            return head

        # [0, 1, 2, 3, 4, 5, 6]
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list
        mid = slow.next
        slow.next = None
        
        rev_list = reverse(mid)

        merge(head, rev_list)