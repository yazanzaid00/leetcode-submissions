# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        pointer_1 = list1
        pointer_2 = list2
        if pointer_1.val < pointer_2.val:
                head = list3 = pointer_1
                pointer_1 = pointer_1.next
        else:
            head = list3 = pointer_2
            pointer_2 = pointer_2.next
        while(pointer_1 and pointer_2):
            if pointer_1.val < pointer_2.val:
                list3.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                list3.next = pointer_2
                pointer_2 = pointer_2.next
            list3 = list3.next
        while(pointer_1):    
            list3.next = pointer_1
            pointer_1 = pointer_1.next
            list3 = list3.next
        while(pointer_2):    
            list3.next = pointer_2
            pointer_2 = pointer_2.next
            list3 = list3.next
        return head
        