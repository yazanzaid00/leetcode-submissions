# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        length = 0
        while curr: 
            curr = curr.next
            length += 1
        index_to_delete = length - n
        
        if index_to_delete < 0:
            return head
        elif index_to_delete == 0:
            return head.next if head else None
        
        prev, curr = None, head

        while curr and index_to_delete > 0:
            prev = curr
            curr = curr.next
            index_to_delete -= 1
        

        # delete curr from the linked list
        if prev:
            prev.next = curr.next
        else:
            # return empty
            return None
        return head
        
