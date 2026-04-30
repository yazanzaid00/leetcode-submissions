# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        linked_list_set = set()
        while current:
            if current in linked_list_set:
                return True
            linked_list_set.add(current)
            current = current.next
        return False
        